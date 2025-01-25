import sqlite3

def create_db():
    # Connect to SQLite database (it will create the database if it doesn't exist)
    conn = sqlite3.connect('vistara.db')
    c = conn.cursor()
    
    # Create table for users (if not exists)
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Call the function to create the database and table
create_db()
