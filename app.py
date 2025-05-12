from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create table if it doesn't exist
def init_db():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    return render_template('success.html', name=name)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
