

class Vertex:
    def __init__(self, key):
        # reflects the id of the vertex node
        # I did not rename 'key' to 'id'
        self.key = key
        # for adjacent key is vertex object, value is weight
        self.adjacent = {}    # renamed per hwk spec
        self.visited = False    # created pe hwk spec
        self.previous = None    # created per hwk spec

    def add_neighbor(self, neighbor, weight=None):
        self.adjacent[neighbor] = weight

    def __str__(self):
        """returns vertex string representation"""
        return '{} neighbors: {}'.format(
            self.key,
            [x.key for x in self.adjacent]
        )

    def get_connections(self):
        """returns vertex objects list
        keys are vertex objects"""
        return self.adjacent.keys()

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    # Accessors
    def getVertexID(self):
        """vertex id accessor"""
        pass

    def getWeight(self):
        """vertex weight accessor"""
        pass

    def getDistance(self):
        """distance accessor"""
        pass

    def getConnections(self):
        """vertex connections accessor"""
        pass

    # Mutators
    def setDistance(self):
        """set distance attribute"""
        pass

    def setPrevious(self):
        """set previous attribute"""
        pass

    def addNeighbor(self):
        """adds vertex neighbor
        id and weight into adjacency list"""
        pass
