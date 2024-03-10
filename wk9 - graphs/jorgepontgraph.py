# Foothill College
# CS 03C - DSs and A in Python, Winter 2024
# Assignment 5 -- graphs
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

from jorgepontvertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    # Accessors
    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def getVertices(self):
        return list(self.vertices.keys())

    # Mutators
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], cost)

    def __contains__(self, n):
        return n in self.vertices

    # Helpers
    def __iter__(self):
        return iter(self.vertices.values())

    def get_num_vertices(self):
        return self.numVertices

    def getEdges(self):
        """generates an inclusive list of from->to: weight of all edges in the graph
        (homework requirement)"""
        list_of_edges = []
        for from_id in self.getVertices():  # vertices keys
            for to_id in self.getVertex(from_id).connectedTo.items():
                #print('from node:', from_id)
                #print('to node:', to_id[0].getId())
                #print('weight:', to_id[1])
                #print('---')
                list_of_edges.append((from_id, to_id[0].id, to_id[1]))
        return list_of_edges


