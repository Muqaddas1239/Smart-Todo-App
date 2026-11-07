# Smart Todo App

A web-based Todo Application developed using Python, Flask, MySQL, HTML, and CSS.

## Project Overview

Smart Todo App is designed to help users organize and manage their daily tasks efficiently. Users can create tasks, add descriptions, set priorities, assign due dates, and track task completion.

## Technologies Used

- Python
- Flask
- MySQL
- HTML
- CSS

## Project Features

- Add and manage tasks
- Write task descriptions
- Set task priorities (High, Medium, Low)
- Assign due dates
- Track task status (Pending and Completed)
- Store tasks in a MySQL database
- User-friendly web interface

## Project Structure

```text
Smart_Todo_App/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── database.py
├── schema.sql
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Muqaddas1239/Smart-Todo-App.git
```

### 2. Open the Project Folder

```bash
cd Smart-Todo-App
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

- Create a MySQL database.
- Configure your database credentials in the `.env` file.
- Run the SQL commands from `schema.sql` to create the required table.

### 7. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Author

**Muqaddas Ameen**

GitHub: [Muqaddas1239](https://github.com/Muqaddas1239)

## Project Status

Under Development
