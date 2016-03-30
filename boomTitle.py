import MySQLdb
import Queue
import sys
from py2neo import authenticate, Graph, Node, Relationship

authenticate("localhost:7474", "neo4j", "gb96bhargav")
graph = Graph()
db = MySQLdb.connect("localhost","root","gb96bhargav","categorytree" )
cursor = db.cursor()
brray=[]

def catquery(pid):

	leafNode = Node("leaf", title = "Sink");
	graph.create(leafNode);

	q = Queue.Queue()
	
	cursor.execute("SELECT cl_to from categorylinks where cl_from=" + str(pid) + ";")
        data = cursor.fetchall()
        for a in data:
                print boomer(a[0])
		catNode = Node("subcat", title = a[0])
		graph.create(catNode)
		rel = Relationship(leafNode, "child of", catNode)
		graph.create(rel)
		brray.append(a[0])
		q.put(a[0])

	while not q.empty():
		s = q.get()
		#fetch the subcat node from neo4j

		r = graph.cypher.execute("MATCH(n:subcat) where n.title = \'" + s + "\' RETURN n")		

		subcatNode = r[0][0]

	#	for resu in subcatNode:
	#		print "The node info obtained after query is " + resu

		cursor.execute("select cl_to from categorylinks where cl_sortkey=\"" + boomer(s) + "\" and cl_type=\"subcat\";")
		data = cursor.fetchall()
		if data != None:
			for a in data:
				flag = 0
#				print "====================================================================="
				for job in brray:
					if job == a[0]:
						flag = 1
						r = graph.cypher.execute("MATCH(n:subcat) where n.title = \'" + a[0] + "\' RETURN n")

						catNode = r[0][0]

						rel = Relationship(subcatNode, "child of", catNode)
						graph.create(rel)
						# inga oru edge to a[0] from s ehtuku?
						# ingayum neo4j
						break
				
#				print "====================================================================="
				if flag == 0:
					print boomer(a[0])
					catNode = Node("subcat", title = a[0])
					graph.create(catNode);
					rel = Relationship(subcatNode, "child of", catNode)
			                graph.create(rel)
					#inga neo4j vertices and edges create pannanum
					q.put(a[0])
					brray.append(a[0])

def query(pid):
	cursor.execute("SELECT cl_to from categorylinks where cl_from=" + str(pid) + " limit 20;")
	data = cursor.fetchall()
	for a in data:
		print boomer(a[0])
		catquery(a[0])

def boomer(st):
	output=""
	for i in st:
		if i == '_':
			output += ' '
		else:
			output += i.upper()
	return output

catquery(sys.argv[1])
#print boomer("Kennieth_Whiting-class_seaplane_tenders")

db.close()
