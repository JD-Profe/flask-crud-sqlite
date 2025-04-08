import sqlite3
import os
from flask import Flask
#from dotenv import load_dotenv

#load_dotenv()

DATABASE = os.getenv('DATABASE', 'tasks.db')

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = DATABASE

    with app.app_context():
        init_db()

    from .routes import main
    app.register_blueprint(main)

    return app

def init_db():
    if not os.path.exists(DATABASE):
        with sqlite3.connect(DATABASE) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    due_date TEXT,
                    status TEXT NOT NULL DEFAULT 'pendiente'
                )
            ''')
