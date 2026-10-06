# create two tables Books and Author

# Books  --bookno,title,author id(foreign),price,pages,published year

# Author ---author_id,name,nationality,birthyear

# 1,Find all books of specific author
# 2.Find the publication year of a particular book
# 3.Find the youngest author
# 4.List books with their corresponding author where booktitle contains a specific keyword
# 5.list all authors who have written books published after a particular year.
import mysql.connector
# conn=mysql.connector.connect(host="localhost",user="root",password="Root")
# c=conn.cursor()
# c.execute("CREATE DATABASE IF NOT EXISTS book")
# print("CREATED")
conn=mysql.connector.connect(host="localhost",user="root",password="Root",database="book")
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Author (AUTHORID INT PRIMARY KEY,NAME VARCHAR(50),NATIONALITY VARCHAR(50),BIRTHYEAR INT)")
c.execute("CREATE TABLE IF NOT EXISTS Books(BOOKNO INT PRIMARY KEY ,TITLE VARCHAR(50),AUTHORID INT,PRICE INT,PAGES INT,PUBLISHED_YEAR INT,FOREIGN KEY(AUTHORID) REFERENCES AUTHOR(AUTHORID))")
conn.commit()
c.execute("""INSERT INTO Books(AUTHORID,NAME,NATIONALITY,BIRTHYEAR") VALUES
    (1,"TITLE1",101,200,50,2020),
    (2,"TITLE2",102,250,70,2022),
    (3,"TITLE3",103,350,86,2025),
    (4,"TITLE2",103,380,95,2017)
    """)
c.execute("""
INSERT INTO Author(author_id, name, nationality, birthyear) VALUES
    (101, 'Author1', 'Indian', 1980),
    (102, 'Author2', 'Indian', 1985),
    (103, 'Author3', 'British', 1975)
""")
conn.commit()
auth=input("enter the author name")
c.execute("SELECT * FROM Books WHERE name = %s"),