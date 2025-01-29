import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/bank.db")
# print("Database connected")

# con.execute("""CREATE TABLE IF NOT EXISTS Bank (
#     bank_id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     location TEXT,
#     swift_code TEXT
# )""")

# con.execute("""CREATE TABLE IF NOT EXISTS Customer (
#     customer_id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     email TEXT,
#     phone TEXT,
#     address TEXT
# )""")

# con.execute("""CREATE TABLE IF NOT EXISTS Account (
#     account_id INTEGER PRIMARY KEY,
#     customer_id INTEGER,
#     bank_id INTEGER,
#     account_type TEXT,
#     balance REAL,
#     FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
#     FOREIGN KEY (bank_id) REFERENCES Bank(bank_id)
# )""")

# con.execute("INSERT INTO Bank VALUES (1, 'CitiBank', 'New York', 'CITIUS33')")
# con.execute("INSERT INTO Bank VALUES (2, 'HSBC', 'London', 'HSBCGB2L')")
# con.execute("INSERT INTO Bank VALUES (3, 'DBS', 'Singapore', 'DBSSSGSG')")

# con.execute("INSERT INTO Customer VALUES (1, 'John Doe', 'john@email.com', '1234567890', 'NY')")
# con.execute("INSERT INTO Customer VALUES (2, 'Jane Smith', 'jane@email.com', '0987654321', 'London')")
# con.execute("INSERT INTO Customer VALUES (3, 'Bob Chen', 'bob@email.com', '5555555555', 'Singapore')")

# con.execute("INSERT INTO Account VALUES (1, 1, 1, 'Savings', 5000.00)")
# con.execute("INSERT INTO Account VALUES (2, 1, 2, 'Checking', 3000.00)")
# con.execute("INSERT INTO Account VALUES (3, 2, 2, 'Savings', 7000.00)")
# con.execute("INSERT INTO Account VALUES (4, 3, 3, 'Investment', 10000.00)")

# con.commit()

# Case 1: Customer with accounts details
cursor = con.execute("""
    SELECT c.name, b.name, a.account_type, a.balance 
    FROM Customer c
    JOIN Account a ON c.customer_id = a.customer_id
    JOIN Bank b ON a.bank_id = b.bank_id
    ORDER BY c.name
""")
print("\nCustomer Accounts:")
for row in cursor:
    print(f"{row[0]} has {row[2]} account at {row[1]} with balance ${row[3]:,.2f}")
    
# Case 2: Banks and their customer deposits
cursor = con.execute("""
    SELECT b.name, COUNT(a.account_id) as num_accounts, SUM(a.balance) as total_deposits
    FROM Bank b
    JOIN Account a ON b.bank_id = a.bank_id
    GROUP BY b.name
""")
print("\nBank Deposits:")
for row in cursor:
    print(f"{row[0]} has {row[1]} accounts with total deposits ${row[2]:,.2f}")

con.close()