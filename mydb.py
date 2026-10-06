import sqlite3

con = sqlite3.connect("Company.db")

# Create table
command = """
CREATE TABLE employee(
    empid INTEGER PRIMARY KEY,
    name VARCHAR(30),
    age INTEGER,
    place VARCHAR(30),
    gender VARCHAR(10),
    designation VARCHAR(30),
    salary INTEGER
)
"""

con.execute(command)
con.execute("DELETE FROM employee")
con.commit()

# Insert records
command = """
INSERT INTO employee(empid, name, age, place, gender, designation, salary)
VALUES
(101, 'Arun', 23, 'EKM', 'Male', 'Developer', 25000),
(102, 'Amal', 25, 'TVM', 'Male', 'Developer', 30000),
(103, 'Anu', 22, 'EKM', 'Female', 'Tester', 20000),
(104, 'Manu', 26, 'TCR', 'Male', 'Developer', 55000)
"""

con.execute(command)

con.commit()
e=con.execute("SELECT * FROM employee")
print(e.fetchall())

print("Table created and records inserted successfully")

#selecting particular attribute from the table
e=con.execute("SELECT name,age FROM employee")
print(e.fetchall())

e=con.execute("SELECT * FROM employee WHERE age <=25 and salary <30000")
print(e.fetchall())

e=con.execute("SELECT * FROM employee WHERE empid != 102")
print(e.fetchall())

e=con.execute("SELECT * FROM employee WHERE place = 'EKM' or age <= 25")
print(e.fetchall())

e=con.execute("SELECT * FROM employee WHERE salary BETWEEN 20000 and 30000")
print(e.fetchall())

e=con.execute("SELECT name,age FROM employee WHERE age between 20 and 25")
print(e.fetchall())

e=con.execute("SELECT name,age FROM employee WHERE name LIKE 'A%'")
print(e.fetchall())

e=con.execute("SELECT name,age FROM employee WHERE name LIKE '%A'")
print(e.fetchall())

e=con.execute("SELECT name,age FROM employee WHERE name LIKE 'A__'")
print(e.fetchall())

e=con.execute("SELECT name,age FROM employee WHERE name LIKE '___A'")
print(e.fetchall())

#employee record with place starting with 'E'
e=con.execute("SELECT * FROM employee WHERE place LIKE 'E%'")
print(e.fetchall())

#employee record having 3 letter placename ending with letter 'm'
e=con.execute("SELECT * FROM employee WHERE place LIKE '__M'")
print(e.fetchall())

#employee record having age<25 and name starting with letter 'A'
e=con.execute("SELECT * FROM employee WHERE age < 25 and name LIKE 'A%' ")
print(e.fetchall())

#employee records having salary=50000 and place starting with 'T'
e=con.execute("SELECT * FROM employee WHERE place LIKE 'T%' and salary = 50000")
print(e.fetchall())

#employee records having age=30 or age=25
e=con.execute("SELECT *FROM employee WHERE age in (25,30)")
print(e.fetchall())

#order by
e=con.execute("SELECT *FROM employee ORDER BY age desc")
print(e.fetchall())

e=con.execute("SELECT *FROM employee ORDER BY age ")
print(e.fetchall())

e=con.execute('select distinct(place) from employee')
print(e.fetchall())

e=con.execute("DELETE FROM employee")
print(e.fetchall())

#Update
con.execute('update employee set name="kiran",age=28 where empid=102')
con.commit()
print("Table updated successfully")

#delete
con.execute("delete from employee where empid=103")
con.commit()
print("Table updated successfully")