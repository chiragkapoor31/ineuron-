
import mysql.connector as com
mydb=com.connect(host="localhost",user="root",passwd="chirag31kapoor")

cursor=mydb.cursor()
#cursor.execute("create database db1")
#cursor.execute("show databases")
#cursor.execute("create table db1.student(rollno int(11),name varchar(20),class int(3),total_marks int(4))")
q2=cursor.execute("select * from db1.student")
print(q2)
print(cursor.fetchall())
