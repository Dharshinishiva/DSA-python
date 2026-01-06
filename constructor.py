# creating an constructor


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        Linked_list = Node(value)
        self.head = Linked_list
        self.tail = Linked_list
        self.length = 1


first = LinkedList(5)
print(first.length)
