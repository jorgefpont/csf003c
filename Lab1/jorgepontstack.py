# Foothill College
# CS 03C - DSs and A in Python, Winter 2024
# Assignment 1
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994
"""
constructor: init head attribute; if data parameter push data onto stack
_x_ push(): push a node on top of the stack
_x_ pop(): remove the top node on the stack
peek(): if top node exists get data
_x_ is_empty() : checks if empty stack
create_stack(): class method to create a Stack
delete_stack(): release all the nodes in the stack.
"""

from jorgepontnode import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        """pushes a node to head (prepend)"""
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """pops head node"""
        # code below pops from tail--need to change
        if self.head is not None:
            res = self.head
            self.head = self.head.next
            return res.getData()
        else:
            return False

    @classmethod
    def create_stack(cls, input_string):
        """Creates a new stack given an input string"""
        ll = cls()
        for token in input_string:
            ll.push(token)
        return ll

    def delete_stack(self):
        """Deletes stack by setting head to None"""
        self.head = None

    def peek(self):
        """Returns head node but does not pop it from the stack"""
        if not self.is_empty():
            return self.head
        else:
            return False

    def print_list(self):
        """Prints the stack"""
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=", ")
            cur_node = cur_node.next
