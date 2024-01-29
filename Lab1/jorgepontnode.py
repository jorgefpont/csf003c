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

    valid_data = "[{()]}"

    def __init__(self, data):
        if self.validate_data(data):
            self.data = data
            self.next = None
        else:
            print("error")


    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next

    def validate_data(self, data):
        if data not in Node.valid_data:
            print("Incorrect data for Node")
        else:
            return True

    def validate_points(self):
        pass

