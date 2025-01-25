import sqlite3

def create_db():
    conn = sqlite3.connect('vistara.db')
    c = conn.cursor()
    
    # Create table to store user data
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # Insert a test user (password should be hashed in practice)
    c.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', ('user123', 'password123'))
    
    conn.commit()
    conn.close()

create_db()
