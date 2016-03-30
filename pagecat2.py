import MySQLdb
db = MySQLdb.connect("localhost","root","gb96bhargav","categorytree" )
cursor = db.cursor()

def boomer(st):
        output=""
        for i in st:
                if i == '_':
                        output += ' '
                else:
                        output += i.upper()
        return output

cursor.execute("SELECT cl_sortkey from categorylinks where cl_type='page';")
data = cursor.fetchall()
arr=[]
for i in data:
	cursor.execute("SELECT cl_to from categorylinks where cl_type=`" + i[0] + "`;")
	temp = cursor.fetchall()
	arr.append((i, temp))
fp = open("dataset3.txt", "w")
fp.write(str(arr))
