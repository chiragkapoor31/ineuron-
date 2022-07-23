
import mysql.connector as com
mydb=com.connect(host="localhost",user="root",passwd="chirag31kapoor")
cursor=mydb.cursor()
cursor.execute("insert into db1.student values(135,'chirag',5,500) ")
cursor.execute("insert into db1.student values(135,'chirag',5,500) ")
cursor.execute("insert into db1.student values(135,'chirag',5,500) ")
cursor.execute("insert into db1.student values(135,'chirag',5,500) ")
mydb.commit()
cursor.execute("select * from db1.student")

for i in cursor.fetchall():
    print(i)
