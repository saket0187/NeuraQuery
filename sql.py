import sqlite3
import random

# Define sample data lists for random generation
first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Evan", "Fiona", "George", "Hannah", "Ian", "Jessica", "Kevin", "Laura", "Michael"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson"]
genders = ["Male", "Female", "Other"]
departments = ["Engineering", "Sales", "HR", "Marketing", "Finance", "IT", "Support", "Operations"]
locations = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]

# Connecting to sqlite (creates the file if it doesn't exist)
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Drop the table if it exists for a fresh start (optional)
cursor.execute("DROP TABLE IF EXISTS EMPLOYEES")

# Creating EMPLOYEES table with 8 columns
create_table_query = """
CREATE TABLE EMPLOYEES (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    gender TEXT,
    department TEXT,
    salary REAL,
    location TEXT
);
"""
cursor.execute(create_table_query)

# Number of rows to insert (876 in this example)
num_rows = 876

# Insert randomly generated employee data
for _ in range(num_rows):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    age = random.randint(21, 65)
    gender = random.choice(genders)
    department = random.choice(departments)
    # Salary range between 30000 and 120000; rounded to nearest whole number
    salary = round(random.uniform(30000, 120000), 2)
    location = random.choice(locations)
    
    insert_query = """
    INSERT INTO EMPLOYEES (first_name, last_name, age, gender, department, salary, location)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    cursor.execute(insert_query, (first_name, last_name, age, gender, department, salary, location))

# Display inserted data count
cursor.execute("SELECT COUNT(*) FROM EMPLOYEES")
count = cursor.fetchone()[0]
print(f"Total records inserted: {count}")

# Optionally, display first 10 rows of data for verification
cursor.execute("SELECT * FROM EMPLOYEES LIMIT 10")
rows = cursor.fetchall()
print("Sample data:")
for row in rows:
    print(row)

# Commit your changes and close the connection
conn.commit()
conn.close()
