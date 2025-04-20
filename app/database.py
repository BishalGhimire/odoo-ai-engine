import sqlite3
from datetime import datetime
import secrets

DB_FILE = "api_keys.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS api_keys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                api_key TEXT NOT NULL UNIQUE,
                created_at TEXT NOT NULL
            )
        ''')
        conn.commit()

def create_api_key(email: str) -> str:
    key = secrets.token_urlsafe(32)
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO api_keys (email, api_key, created_at)
            VALUES (?, ?, ?)
        ''', (email, key, datetime.utcnow().isoformat()))
        conn.commit()
    return key

def is_valid_key(api_key: str) -> bool:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM api_keys WHERE api_key = ?', (api_key,))
        return cursor.fetchone() is not None
