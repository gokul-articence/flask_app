from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    records = cursor.fetchall()
    conn.close()
    return render_template("index.html", records=records)

@app.route('/mark', methods=['POST'])
def mark_attendance():
    name = request.form['name']
    date = request.form['date']
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (name, date) VALUES (?, ?)", (name, date))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True,host="0.0.0.0")
