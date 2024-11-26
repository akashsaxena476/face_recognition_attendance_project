import sqlite3

conn = sqlite3.connect('attendance.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS attendance (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    id INTEGER,
    name TEXT,
    timestamp TEXT,
    UNIQUE(id, timestamp)
)
''')
conn.commit()
conn.close()
