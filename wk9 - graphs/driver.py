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
        print()

for v in g:
    print(v)

print('Nuber of vertices: ', g.get_num_vertices())

print('vertices dictionary:', g.getEdges())

for from_id in g.get_vertices():
    print('from_id:', from_id)
    t = tuple(f"{v.id}:{weight}" for v, weight in
              g.get_vertex(from_id).adjacent.items())
    print(f"edge; {from_id} to {t}")


