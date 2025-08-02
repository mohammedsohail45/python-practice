My first project on GitHub
# Backend API Project – Internship Assignment

This project is a backend API developed using **FastAPI**, designed during internship as part of a practical assignment. It supports user management and personal information storage with proper routing, models, and database integration.

---

## 🚀 Tech Stack

- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy**
- **SQLite** (or other DB via `.env`)
- **Pydantic**
- **Uvicorn**
- **Postman** (for API testing)

---

## 📁 Folder Structure
app/
├── crud/ # Database operation functions
├── models/ # SQLAlchemy DB models
├── routers/ # Route handlers (API endpoints)
├── schemas/ # Pydantic validation models
├── database.py # DB connection logic
├── main.py # FastAPI entry point


---

## 🔐 .env (Environment File)

DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_secret_key_here


## 📦 Installation & Run

```bash
# Clone repo
git clone https://github.com/yourusername/yourrepo.git

# Navigate
cd mohammed_sohail_api_assignment

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload

🔌 API Endpoints (Examples)
Method	Endpoint	Description
POST	/register	Register new user
POST	/login	Login user
GET	/personal_info/{id}	Get personal info by ID
POST	/personal_info/	Add personal info

Test API using Postman
Use mohammed_sohail_postman_collection.json for ready API tests.

🙋‍♂️ Author
Mohammed Sohail
BCA Graduate | FastAPI, Python, HTML, PHP Developer



