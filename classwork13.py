# Create a database file school.db
#
# create a table Student with fields roll_no(pk),name,age,gender,course,mark
#
# write a menu driven code
#
#                     1.Insert Student details
#                     2.Read all student details
#                     3.search a student by rollno
#                     4.update the mark of a student
#                     5.Delete a student record
#                     6.Exit
import mysql.connector
conn=mysql.connector.connect(user="root",password="Root",host="localhost")
c=conn.cursor()
c.execute("CREATE DATABASE IF NOT EXISTS SCHOOL")
c.execute("USE SCHOOL")
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS Student(ROLL_NO INT PRIMARY KEY,NAME VARCHAR(20),AGE INT,GENDER VARCHAR(20),COURSE VARCHAR(20),MARK INT)""")
print("TABLE CREATED")
conn.commit()
def insert_record():
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    course = input("Enter Course: ")
    mark = int(input("Enter Mark: "))

    insert=("""INSERT INTO Student(ROLL_NO,NAME,AGE,GENDER,COURSE,MARK) VALUES
    (%s,%s,%s,%s,%s,%s)""")
     
    values = (roll_no, name, age, gender, course, mark)
    c.execute(insert,values)

    print("INSERTED SUCCESSFULLY")
    conn.commit() 
def student():
    c.execute("SELECT * FROM Student")
    a=c.fetchall()
    print(a)
def search_by_rollno():
    search=input("Enter the roll no : ")
    c.execute("SELECT * FROM Student WHERE ROLL_NO =  %s", (search,))
    a=c.fetchone()
    if a:
        print(a)
    else:
        print("NOT FOUND")
def update_mark():
    search=input("Enter the roll no : ")
    mark=input("Enter the updated mark : ")
    c.execute("SELECT * FROM Student WHERE ROLL_NO =  %s", (search,))
    a=c.fetchone()
    if a:
        c.execute("UPDATE Student SET MARK = %s  WHERE ROLL_NO =  %s", (mark,search,))
        print(a)
        conn.commit()
    else:
        print("NOT FOUND")
def delete_record():
    search = int(input("Enter the roll no: "))

    c.execute("SELECT * FROM Student WHERE ROLL_NO = %s",(search,))
    k = c.fetchone()
    if k:
        c.execute("DELETE FROM Student WHERE ROLL_NO = %s",(search,))
        conn.commit()
        print("DELETED")
    else:
        print("STUDENT NOT FOUND")
while(1):
    print("1.INSERT INTO TABLE\n2.DISPLAY TABLE\n3.SEARCH BY ROLL NO\n4.UPDATE MARK\n5.DELETE RECORD\n6.EXIT")
    ch=int(input("ENTER YOUR CHOICE : "))
    if ch == 1:
        insert_record()
    elif ch ==2:
        student()
    elif ch ==3:
        search_by_rollno()
    elif ch ==4:
        update_mark()
    elif ch ==5:
        delete_record()
    else:
        exit()
