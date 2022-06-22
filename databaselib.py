import sqlite3

conn = None 
try:
    conn = sqlite3.connect("CaptureDB.db")
    print(sqlite3.version)
except sqlite3.Error as e:
    print(e)
finally:
    if conn:
        conn.close()