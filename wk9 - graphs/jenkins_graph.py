#
#  adjGraph
#
#  Created by Brad Miller on 2005-02-24.
#  Copyright (c) 2005 Brad Miller, David Ranum, Luther College. All rights reserved.
#

import sys
import os
import unittest


class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t], cost)

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())

    def getEdges(self):
        list_of_edges = []
        for from_id in g.getVertices():  # vertices keys
            # print('from node:', from_id)
            for to_id in g.getVertex(from_id).connectedTo.items():
                print('from node:', from_id)
                # print('to node:', to_id[0].id)
                print('to node:', to_id[0].getId())
                print('weight:', to_id[1])
                print('---')
                list_of_edges.append((from_id, to_id[0].id, to_id[1]))
        return list_of_edges


class Vertex:
    def __init__(self, num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0

    # def __lt__(self,o):
    #     return self.id < o.id

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.dist = d

    def setPred(self, p):
        self.pred = p

    def setDiscovery(self, dtime):
        self.disc = dtime

    def setFinish(self, ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(
            self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred) + "]\n"

    def getId(self):
        return self.id


# class adjGraphTests(unittest.TestCase):
#     def setUp(self):
#         self.tGraph = Graph()
#
#     def testMakeGraph(self):
#         gFile = open("test.dat")
#         for line in gFile:
#             fVertex, tVertex = line.split('|')
#             fVertex = int(fVertex)
#             tVertex = int(tVertex)
#             self.tGraph.addEdge(fVertex, tVertex)
#         for i in self.tGraph:
#             adj = i.getAdj()
#             for k in adj:
#                 print(i, k)


if __name__ == '__main__':
    #unittest.main()
    g = Graph()
    g.addEdge('V0', 'V1', 5)
    g.addEdge('V0', 'V5', 2)
    g.addEdge('V1', 'V2', 4)
    g.addEdge('V2', 'V3', 9)
    g.addEdge('V3', 'V4', 7)
    g.addEdge('V3', 'V5', 3)
    g.addEdge('V4', 'V0', 1)
    g.addEdge('V5', 'V2', 1)
    g.addEdge('V5', 'V4', 8)

    for from_id in g.getVertices():
        print('***from_id:', from_id)
        t = tuple(f'{v.id}:{cost}' for v, cost in
                  g.getVertex(from_id).connectedTo.items())
        print(f'edge: {from_id} to : {t}')
        print('***tuple:', t)

    # res = []
    # for from_id in g.getVertices():  # vertices keys
    #     #print('from node:', from_id)
    #     for to_id in g.getVertex(from_id).connectedTo.items():
    #         print('from node:', from_id)
    #         #print('to node:', to_id[0].id)
    #         print('to node:', to_id[0].getId())
    #         print('weight:', to_id[1])
    #         print('---')
    #         res.append((from_id, to_id[0].id, to_id[1]))
    #
    # print(res)

    print('***', g.getEdges())





