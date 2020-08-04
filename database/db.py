import sqlite3

conn = sqlite3.connect("test.db")
conn.execute("CREATE TABLE email (id integer pk, email String(80) unique)")
conn.commit()