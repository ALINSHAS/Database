# 1.Create a table named students to store student information.
# Table: students
# Column Name
# Data Type
# Description
#
# student_id
# INT (Primary Key)
# Unique student ID
#
# name
# VARCHAR(100)
# Name of the student
#
# age
# INT
# Age of the student
#
# gender
# VARCHAR(10)
# Gender
#
# course
# VARCHAR(100)
# Enrolled course
#
# marks
# INT
# Marks obtained
#
# city
# VARCHAR(100)
# City of the student
import sqlite3
conn = sqlite3.connect("Students.db")
# # Create table
# command = """
# CREATE TABLE IF NOT EXISTS students(
#     student_id INTEGER PRIMARY KEY,
#     name VARCHAR(100),
#     age INTEGER,
#     gender VARCHAR(100),
#     course VARCHAR(100),
#     mark INTEGER,
#     city VARCHAR(100)
# )
# """
# conn.execute(command)
# # Insert records
# command = """
# INSERT INTO students
# (student_id, name, age, gender, course, mark, city)
# VALUES
# (101, 'Rahul', 20, 'Male', 'Computer Science', 85, 'EKM'),
# (102, 'Anjali', 19, 'Female', 'Electronics', 92, 'TVM'),
# (103, 'Arun', 21, 'Male', 'Mechanical', 78, 'EKM'),
# (104, 'Sneha', 20, 'Female', 'Civil', 88, 'TVM'),
# (105, 'Akash', 22, 'Male', 'Computer Science', 95, 'EKM');
# """
# conn.execute(command)
# conn.commit()
# Questions
# Display all records from the students table.
# e=conn.execute("SELECT * FROM students ")
# print(e.fetchall())
# Display name, course, and marks for all students.
# e=conn.execute("SELECT name,course,mark FROM students ")
# print(e.fetchall())
# Display names and marks of students who scored more than 80.
# e=conn.execute("SELECT name,mark FROM students WHERE mark > 80 ")
# print(e.fetchall())
# Display all details of students enrolled in Computer Science.
# e=conn.execute("SELECT * FROM students WHERE course = 'Computer Science'")
# print(e.fetchall())
# Display names, ages, and cities of students whose age is between 18 and 22.
# e=conn.execute("SELECT name,age,city FROM students WHERE age BETWEEN 18 and 25 ")
# print(e.fetchall())
# # Display names, marks, and courses of students from Kochi, sorted by marks in descending order.
# e=conn.execute("SELECT name,mark,course FROM students WHERE city = 'EKM' ORDER BY mark DESC")
# print(e.fetchall())
# Insert a new record into the students table.
# command="""INSERT INTO students(student_id, name, age, gender, course, mark, city) VALUES (106,'ALTHAF',22,'MALE','BCA',90,'KOLLAM') """
# conn.execute(command)
# conn.commit()
# # Update marks of all students who scored below 50 by adding 5 bonus marks.
# conn.execute("UPDATE students SET mark = mark + 5 WHERE mark < 50")
# conn.commit()
# # Delete all student records where marks are less than 35.
# conn.execute("DELETE  FROM students WHERE mark < 35")
# conn.commit()