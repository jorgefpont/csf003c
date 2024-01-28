# Foothill College
# CS 03C - DSs and A in Python, Winter 2024
# Assignment 1
# Prepared by Jorge Pont
# Email: jorgefpont@gmail.com
# Student ID: 10949994

# Driver code

from jorgepontstack import LinkedList

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.print_list()
print()
llist.push("hello")
llist.print_list()
print()
llist.pop()
llist.print_list()
print()
print("is empty: ", llist.is_empty())
test_s = "[[]]{}()"
ll2 = LinkedList.create_stack(test_s)
ll2.print_list()
print()