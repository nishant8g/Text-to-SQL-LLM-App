import sqlite3

##connect to sqlite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record,create table,retrieve
cursor=connection.cursor()

##create the table
table_info="""
create table students(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

#insert some more records

cursor.execute("INSERT INTO students VALUES ('John Smith', 10, 'A', 85)")
cursor.execute("INSERT INTO students  VALUES ('Priya Sharma', 9, 'B', 92)")
cursor.execute("INSERT INTO students  VALUES ('Ahmed Khan', 11, 'C', 78)")
cursor.execute("INSERT INTO students  VALUES ('Maria Gonzalez', 12, 'D', 88)")

#display all the records
print("The inserted records are")
data=cursor.execute("SELECT * FROM students")


for row in data:
    print(row)

##close the connection

connection.commit()
connection.close()

