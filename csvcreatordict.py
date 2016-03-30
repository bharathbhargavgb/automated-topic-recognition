import MySQLdb
import Queue
import sys
from progressbar import ProgressBar
from py2neo import authenticate, Graph, Node, Relationship

pb = ProgressBar()
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
fp = open("subcatnodes.csv", "w")
fp.write("id,title\n")
i=0
dicto={}
for node in pb(nodes):
	fp.write(str(i)+"," + str("subcat" + boomer(node[0]) + str("\n")))
	dicto[str("subcat"+boomer(node[0]))] = i

	i=i+1
	
pb = ProgressBar()

cursor.execute("select distinct cl_sortkey from categorylinks where cl_type='page';");
nodes = cursor.fetchall()


for node in pb(nodes):
	fp.write(str(i)+"," + str("page" + boomer(node[0]) + str("\n")))
	dicto[str(("page"+boomer(node[0])))] = i


	i=i+1

cursor.execute("SELECT cl_sortkey, cl_to, cl_type from categorylinks;")
rels = cursor.fetchall()
downlinks = open("downlinks.csv", "w")
uplinks = open("uplinks.csv", "w")
e = 0
uplinks.write("sid1,sid2,uplink\n")

downlinks.write("sid1,sid2,downlink\n")
orphan = open("orphans", "w")
 
pb = ProgressBar()
for rel in pb(rels):
#	print dicto[7]
#	print dicto.index('0S BIRTHS')
#	print dicto.index(str([rel[0]]))
	try:
		parent = dicto[str('subcat'+boomer(rel[1]))]
		child = dicto[str(rel[2]+boomer(rel[0]))]
	except KeyError:
#		orphan.write(boomer(rel[0]) + " " + boomer(rel[1]))
		e=e+1
		continue
	else:
		#fp.write(str(dicto.index(boomer(rel[0]))) + "," + str(dicto.index(boomer(rel[1]))) + ",child_of\n")
		#fp.write(str(dicto.index(boomer(rel[1]))) + "," + str(dicto.index(boomer(rel[0]))) + ",parent_of\n")
	
		uplinks.write(str(child) + "," + str(parent) + ",child_of\n")
		downlinks.write(str(parent) + "," + str(child) + ",parent_of\n")
print e
