# Backend API Assignment – Python (FastAPI + SQLite)

This project is a backend API system built using **Python** with **FastAPI**, and uses **SQLite** as the database. It was created as part of an internship assignment to implement CRUD operations for user and personal information.

## 🔧 Technologies Used

- Python 3
- FastAPI
- SQLite
- Pydantic
- Uvicorn (for running the server)

## 📁 Project Structure

📦 python-practice/
├── main.py # Entry point to run the app
├── database.py # DB connection and setup
├── user.py # User model/schema
├── user_crud.py # User CRUD operations
├── personal_info.py # Personal info model/schema
├── personal_info_crud.py # Personal info CRUD operations
├── init.py
└── README.md

markdown
Copy
Edit

## 🚀 How to Run

1. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn
Run the app:

bash
Copy
Edit
uvicorn main:app --reload
API Docs available at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

📌 Features
Add new user

View user list

Update/delete user

Add and manage personal info

Modular file structure

📬 Contact
Mohammed Sohail
https://github.com/mohammedsohail45

Copy
Edit
