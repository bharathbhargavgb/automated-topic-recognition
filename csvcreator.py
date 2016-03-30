import MySQLdb
import Queue
import sys
from py2neo import authenticate, Graph, Node, Relationship

authenticate("localhost:7474", "neo4j", "gb96bhargav")
graph = Graph()
db = MySQLdb.connect("localhost","root","gb96bhargav","categorytree" )
cursor = db.cursor()
nodes=[]
n=1
def boomer(st):
        output=""
        for i in st:
                if i == '_':
                        output += ' '
		
		else: 
			if i == '\'':
				output += '^'
                	else:
                        	output += i.upper()
        return output

cursor.execute("select distinct cl_to from categorylinks;");
nodes = cursor.fetchall()
n = len(nodes)
fp = open("subcatnodes", "w")
fp.write("id,title\n")
i=0
dicto=[]
for node in nodes:
	fp.write(str(i)+"," + str(boomer(node[0]) + str("\n")))
	dicto.append("subcat"+boomer(node[0]))

	i=i+1


cursor.execute("select distinct cl_sortkey from categorylinks where cl_type='page';");
nodes = cursor.fetchall()


for node in nodes:
	fp.write(str(i)+"," + str(boomer(node[0]) + str("\n")))
	dicto.append("page"+boomer(node[0]))

	i=i+1

cursor.execute("SELECT cl_sortkey, cl_to, cl_type from categorylinks;")
rels = cursor.fetchall()
fp = open("links", "w")
e = 0
fp.write("subcatnodesId,subcatnodesId,link\n")
orphan = open("orphans", "w") 
for rel in rels:
#	print dicto[7]
#	print dicto.index('0S BIRTHS')
#	print dicto.index(str([rel[0]]))
	try:
		parent = dicto.index('subcat'+boomer(rel[0]))
		child = dicto.index(rel[2]+boomer(rel[1]))
	except ValueError:
#		orphan.write(boomer(rel[0]) + " " + boomer(rel[1]))
		e=e+1
		continue
	else:
		#fp.write(str(dicto.index(boomer(rel[0]))) + "," + str(dicto.index(boomer(rel[1]))) + ",child_of\n")
		#fp.write(str(dicto.index(boomer(rel[1]))) + "," + str(dicto.index(boomer(rel[0]))) + ",parent_of\n")
	
		fp.write(str(child) + "," + str(parent) + ",child_of\n")
		fp.write(str(parent) + "," + str(child) + ",parent_of\n")
print e
