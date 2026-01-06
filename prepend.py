# adding element as first element


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, value):
        first_node = Node(value)
        self.head = first_node
        self.tail = first_node
        self.length = 0

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def prepend(self, value):
        first_node = Node(value)
        if self.head is None:
            self.head = first_node
            self.tail = first_node

        else:
            first_node.next = self.head
            self.head = first_node

    def append(self, value):
        first_node = Node(value)
        if self.head is None:  # if linked list is empty
            self.head = first_node
            self.tail = first_node

        else:
            self.tail.next = first_node
            self.tail = first_node
        self.length += 1


my_linkedlist = Linkedlist(4)

my_linkedlist.append(8)
my_linkedlist.append(12)
my_linkedlist.print()

my_linkedlist.prepend(2)
my_linkedlist.print()
