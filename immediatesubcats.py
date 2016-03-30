from py2neo import authenticate, Graph, Node, Relationship
authenticate("localhost:7474", "neo4j", "gb96bhargav")
graph = Graph()

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

recordlist = graph.cypher.execute("MATCH (Subcat { id:17735})-[r:parent_of]->(child) RETURN child")
#print recordlist
catcontents=[]
for r in recordlist:
	article_title = r[0].properties["title"]	
#	print article_title
#	print "hello"
	if article_title[0] == 's':
		catcontents.append((r[0].properties['id'],article_title[6:]))
print catcontents
print len(catcontents)
