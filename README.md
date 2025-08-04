# expense_tracker
I built this simple expense tracker using Python, Flask, and SQL to practice my full-stack skills. It's a practical tool that lets you log, categorize, and delete daily expenses while keeping a running total.


# Technologies
  Backend:Python, Flask
  Database:SQLite
  Frontend:HTML, CSS

# How to Run
```bash
# 1. Clone this repository
git clone https://github.com/keshavkumarb/expense_tracker
cd expense_tracker

# 2. Set up the environment and install dependencies
python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate
pip install -r requirements.txt

# 3. Initialize the database (run this only once)
python init_db.py

# 4. Run the app
flask run
