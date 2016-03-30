import MySQLdb
import Queue
import sys
from py2neo import authenticate, Graph, Node, Relationship

authenticate("localhost:7474", "neo4j", "gb96bhargav")
graph = Graph()
db = MySQLdb.connect("localhost","root","gb96bhargav","categorytree" )
cursor = db.cursor()

def boomer(st):
        output=""
        for i in st:
                if i == '_':
                        output += ' '
		if i == '\'':
			output += '^'
                else:
                        output += i.upper()
        return output


cursor.execute("SELECT cl_sortkey, cl_to from categorylinks;")
data = cursor.fetchall()
for a in data:
	flag = 0
	recordlist = graph.cypher.execute("MATCH(n:subcat) where n.title = \'" + boomer(a[0]) + "\' RETURN n")
	for r in recordlist:
		catNode1 = r[0]
		flag = 1
	if flag == 0:
		catNode1 = Node("subcat", title=boomer(a[0]))
		graph.create(catNode1)

	flag = 0
	recordlist = graph.cypher.execute("MATCH(n:subcat) where n.title = \'" + boomer(a[1]) + "\' RETURN n")
        for r in recordlist: 
                catNode2 = r[0]
		flag = 1
	if flag == 0:
		catNode2 = Node("subcat", title=boomer(a[1]))
		graph.create(catNode2)

	rel = Relationship(catNode1, "child of" , catNode2)
	graph.create(rel)
