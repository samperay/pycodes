import sqlite3
conn = sqlite3.connect("employee.db")
print("Emp DB created successfully")
conn.execute("create table Employees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")
print("Employee table created successfully")