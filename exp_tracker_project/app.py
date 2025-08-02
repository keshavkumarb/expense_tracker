import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row 
    return conn


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        description = request.form['description']
        category = request.form['category']
        amount = float(request.form['amount'])
        date = datetime.now().strftime("%Y-%m-%d") 

        
        conn = get_db_connection()
        conn.execute('INSERT INTO expenses (date, description, category, amount) VALUES (?, ?, ?, ?)',
                     (date, description, category, amount))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    
    conn = get_db_connection()
    expenses = conn.execute('SELECT * FROM expenses ORDER BY date DESC').fetchall()
    total_expenses = conn.execute('SELECT SUM(amount) FROM expenses').fetchone()[0]
    conn.close()
    
   
    if total_expenses is None:
        total_expenses = 0
        
    return render_template('index.html', expenses=expenses, total_expenses=total_expenses)


@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM expenses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)