
"""
Instance (Private) Attributes

_d_ vertDictionary - mapping of adjacency lists; initialize to empty
_d_ numVertices - number of vertices in graph; initialize to 0

Instance (Public) Methods

Accessors
_d_ getVertex - get vertex id identified by parameter
_d_ getVertices - accessor for all vertices of graph

Mutators
_d_ addVertex - adds a vertex node to the graph
_d_ add Edge - adds a  directed weighted edge
__pass__ setPrevious - sets previous attribute of the current parameter

Helpers
_d_ iterator to access all nodes in graph
__pass__  getEdges - generates an inclusive list of from->to: weight of all edges in the graph

"""

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def add_vertex(self, vertex):
        """adds a vertex node to the graph"""
        self.vertices[vertex.key] = vertex
        self.numVertices += 1

    def get_vertex(self, key):
        """get vertex id identified by parameter"""
        if key in self.vertices[key]:
            return self.vertices[key]
        else:
            return None

    def __contains__(self, key):
        """
        Overload the in operator to support:
          >>> g = Graph()
          >>> g.add_vertex(Vertex(42))
          >>> 42 in g
          True
        """
        return key in self.vertices

    def add_edge(self, from_key, to_key, weight=None):
        """adds a  directed weighted edge"""
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbor(
            self.vertices[to_key],
            weight
        )

    def get_vertices(self):
        """accessor for all vertices of graph"""
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def setPrevious(self):
        """sets previous attribute of the current parameter"""
        pass

    def getEdges(self):
        """generates an inclusive list of from->to: weight of all edges in the graph"""
        pass