import MySQLdb

db = MySQLdb.connect("localhost","root","gb96bhargav","categorytree" )
cursor = db.cursor()

cursor.execute("SELECT distinct(cl_to) from categorylinks where cl_type=\"page\";")
data = cursor.fetchall()

for a in data:
	print a[0]
