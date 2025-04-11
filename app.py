from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('users.db')
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('home.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        conn = sqlite3.connect('users.db')
        conn.execute('INSERT INTO users (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5050, debug=True)

