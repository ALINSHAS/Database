#CREATE A NEW TABLE 
# import mysql.connector
# conn=mysql.connector.connect(user="root",password="Root",host="localhost")
# c=conn.cursor()
# c.execute("CREATE DATABASE mydb")
# print("CREATED")

#TABLE TO A EXISTING FILE
import mysql.connector
conn=mysql.connector.connect(user="root",password="Root",host="localhost",database="mydb")
c=conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS employee (
    empid INT PRIMARY KEY,
    name VARCHAR(20),
    age INT,
    salary INT,
    gender VARCHAR(20),
    place VARCHAR(20)
)
""")
print('Table created')
# c.execute("""INSERT INTO employee(empid,name,age,salary,gender,place) VALUES 
# (101,"ARUN",23,25000,"MALE","EKM"),
# (102, "AMAL",25,30000, "MALE","TVM"),
# (103 ,"ANU",22,35000, "FEMALE","TVM" ),
# (104,"MANU",26,40000, "FEMALE","TCR" )""")
# conn.commit()
# print("Table inserted")
# c.execute("SELECT * FROM employee")
# k=c.fetchall()
# print(k)

#NAME,AGE FROM EMPLOYEE
# c.execute("SELECT name,age FROM employee")
# k=c.fetchall()
# print(k)

#EMPLOYEE RECORD WITH SALARY > 50000
