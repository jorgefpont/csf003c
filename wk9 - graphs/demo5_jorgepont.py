# Foothill College
# CS 03C - DSs and A in Python, Winter 2024
# Assignment 5 -- graphs
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

from jorgepontvertex import Vertex
from jorgepontgraph import Graph

g = Graph()
for i in ['a', 'b', 'c', 'd', 'e']:
    g.addVertex(Vertex(i))

# from homework spec:
# a->b: 4; a->c: 1 ; b->a: 3; b->d: 2; c-> a: 1; c->b: 5

g.addEdge('a', 'b', 4)
g.addEdge('a', 'c', 1)
g.addEdge('b', 'a', 3)
g.addEdge('b', 'd', 2)
g.addEdge('c', 'a', 1)
g.addEdge('c', 'b', 5)

print('\nNumber of vertices: ', g.get_num_vertices(), '\n')
print('list of from->to: weight of all edges in the graph:\n', g.getEdges())


"""
/usr/bin/python3 /home/jorge/jorge-files/Foothill-courses/csf003c/csf003c/wk9 - graphs/demo5_jorgepont.py 

Number of vertices:  9 

list of from->to: weight of all edges in the graph:
 [('a', 'b', 4), ('a', 'c', 1), ('b', 'a', 3), ('b', 'd', 2), ('c', 'a', 1), ('c', 'b', 5)]

Process finished with exit code 0
"""