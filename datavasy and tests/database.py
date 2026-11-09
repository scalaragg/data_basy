import mysql.connector
import pymysql.cursors

connetion = pumysql.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "academy",
    cursorclass = pymysql.cursors.DictCursor
)
cursor = connetion.cursor()
sql = 'INSERT INTO classes(class_name, places) VALUES (%s, %s)'
with connetion.cursor() as cursor:
    cursor.execute(sql,("yellow 403", "20"))
    connetion.commit()
result = cursor.fetchone()

cursor.close()
connetion.close()