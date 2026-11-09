
from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_connection
from datetime import date

app = Flask(__name__)
app.secret_key = "todo_app_secret_key"


@app.route("/")
def index():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
    tasks = cursor.fetchall()

    cursor.close()
    connection.close()

    today = date.today()

    total_tasks = len(tasks)

    completed_tasks = sum(
        1 for task in tasks
        if task["status"] == "Completed"
    )

    pending_tasks = sum(
        1 for task in tasks
        if task["status"] == "Pending"
    )

    due_today_tasks = [
        task for task in tasks
        if task["status"] == "Pending"
        and task["due_date"] == today
    ]

    overdue_tasks = [
        task for task in tasks
        if task["status"] == "Pending"
        and task["due_date"] is not None
        and task["due_date"] < today
    ]

    upcoming_tasks = [
        task for task in tasks
        if task["status"] == "Pending"
        and task["due_date"] is not None
        and task["due_date"] > today
    ]

    return render_template(
        "index.html",
        tasks=tasks,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        due_today_tasks=due_today_tasks,
        overdue_tasks=overdue_tasks,
        upcoming_tasks=upcoming_tasks,
        today=today
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    priority = request.form.get("priority", "Medium")
    due_date = request.form.get("due_date") or None

    if not title:
        flash("Task title is required.")
        return redirect(url_for("index"))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, description, priority, due_date)
        VALUES (%s, %s, %s, %s)
        """,
        (title, description, priority, due_date)
    )

    connection.commit()
    cursor.close()
    connection.close()

    flash("Task added successfully!")
    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET status = CASE
            WHEN status = 'Pending' THEN 'Completed'
            ELSE 'Pending'
        END
        WHERE id = %s
        """,
        (task_id,)
    )

    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))

    connection.commit()
    cursor.close()
    connection.close()

    flash("Task deleted.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
