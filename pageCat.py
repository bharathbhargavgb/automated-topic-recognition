import pdb
import MySQLdb
db = MySQLdb.connect("localhost","root","gb96bhargav","categorytree" )
cursor = db.cursor()

cursor.execute("SELECT cl_sortkey, cl_to from categorylinks where cl_type=\"page\";")
data = cursor.fetchall()
#pdb.set_trace()
#def boomer(st):
#        output=""
#        for i in st:
#                if i == '_':
#                        output += ' '
#                else:
#                        output += i.upper()
#        return output

arr = []

for a in data:
#	cursor.execute("SELECT cl_to from categorylinks where cl_type=\'subcat\' and cl_sortkey=\'"+boomer(a[1])+"\';")
#	data2 = cursor.fetchall()
#n	for b in data2:
		arr.append((a[0],a[1]))
fp = open("data2.txt","w")
fp.write(str(arr))
