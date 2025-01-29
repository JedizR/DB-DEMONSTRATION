import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/bank.db")
# print("Database connected")

con.execute("""CREATE TABLE IF NOT EXISTS Bank (
    bank_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT,
    swift_code TEXT
)""")

con.execute("""CREATE TABLE IF NOT EXISTS Customer (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    address TEXT
)""")

con.execute("""CREATE TABLE IF NOT EXISTS Account (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    bank_id INTEGER,
    account_type TEXT,
    balance REAL,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (bank_id) REFERENCES Bank(bank_id)
)""")

con.commit()