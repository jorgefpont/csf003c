"""
Will contain: a constructor, set methods (data field and next field),
get methods, and a helper method
to determine if the node points to another node.
__x__ constructor: init data and next attributes
__x__ setters: validate parameters before changing state of private attribute;
returns a boolean value if valid parameter
__x__ getters: return attributes
helper methods:  validate parameter data;
checks if a node points to another node
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def validate_data(self):
        pass

    def validate_points(self):
        pass
