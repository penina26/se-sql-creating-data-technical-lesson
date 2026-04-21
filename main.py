import sqlite3
import pandas as pd

conn = sqlite3.connect('my_database.db')

cur = conn.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            signup_date DEFAULT CURRENT_DATE);
''')

# cur.execute('''
# ALTER TABLE users IF NOT EXISTS ADD COLUMN phone_number TEXT;
# ''')

print(cur.execute('''
PRAGMA table_info(users);
''').fetchall())

cur.execute('''
INSERT INTO users (name,email) VALUES 
('Alice','alice@example.com'),
('Bob','bob@example.com');
            
''')
cur.execute('''
            UPDATE users SET phone_number = '123-456-7890' WHERE name = 'Alice';
''')


# conn.commit()

print(cur.execute('''
SELECT * FROM users;
''').fetchall())

cur.execute('''
DELETE FROM users WHERE name = "Bob";''')


conn.close()