from vertex import Vertex
from graph import Graph

g = Graph()
for i in ['a', 'b', 'c', 'd', 'e']:
    g.add_vertex(Vertex(i))

print(g.vertices)

# from homework spec:
# a->b: 4; a->c: 1 ; b->a: 3; b->d: 2; c-> a: 1; c->b: 5

g.add_edge('a', 'b', 4)
g.add_edge('a', 'c', 1)
g.add_edge('b', 'a', 3)
g.add_edge('b', 'd', 2)
g.add_edge('c', 'a', 1)
g.add_edge('c', 'b', 5)

for v in g:
    for w in v.get_connections():
        print("({} -> {})".format(v.key, w.key))

for v in g:
    print(v)


