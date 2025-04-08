from flask import Blueprint, render_template, request, redirect, url_for, current_app
import sqlite3
from datetime import datetime

main = Blueprint('main', __name__)

def get_db_connection():
    conn = sqlite3.connect(current_app.config['DATABASE'])
    return conn

@main.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
def add_task():
    description = request.form['description']
    due_date = request.form['due_date']
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = get_db_connection()
    conn.execute("INSERT INTO tasks (description, created_at, due_date) VALUES (?, ?, ?)",
                 (description, created_at, due_date or None))
    conn.commit()
    conn.close()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:task_id>')
def complete_task(task_id):
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET status = 'completada' WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('main.index'))
