# dating_app
Finds potential matches based on your profile

## Getting Started
**1. Clone the repository**
```zsh
git clone https://github.com/Pankajjangra77/dating_app.git
```
**2. Install python if not, then create a virtual environment**
I have used python3.12 version
```zsh
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```zsh
pip install -r requirements.txt
```
**4. Connect Databse**
```zsh
Add your database connection string in database.py file
```

**5. Start FastAPI application**
```zsh
uvicorn main:app --reload
```
**5. Open local API docs [http://localhost:8000/docs]**
