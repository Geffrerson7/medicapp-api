# 🚀 Medicapp API

This is a RESTful API built with **FastAPI**, designed to provide high-performance endpoints with modern Python async capabilities.

## ⚙️ Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/your-fastapi-project.git
cd your-fastapi-project
```
### 2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
### 4. Apply database migrations:
```bash
alembic upgrade head
```
### 5. Run the API:
```bash
uvicorn app.main:app --reload
```