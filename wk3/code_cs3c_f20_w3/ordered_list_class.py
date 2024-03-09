from node_class import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end = ", ")
            cur_node = cur_node.next

if __name__ == '__main__':
    l = [1, 2, 4, 6, 8, 10, 12]
    lst = OrderedList()
    for i in l:
        lst.add(i)

    lst.print_list()
    print()
    lst.add(5)
    lst.print_list()
    print()
    lst.remove(10)
    lst.print_list()
    print()
    lst.remove(100)