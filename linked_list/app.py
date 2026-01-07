# for appending an element in the end


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

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        first_node = Node(value)
        if self.head is None:  # if linked list is empty
            self.head = first_node
            self.tail = first_node

        else:
            self.tail.next = first_node
            self.tail = first_node
        self.length += 1


my_linkedlist = LinkedList(4)

my_linkedlist.append(8)
my_linkedlist.append(12)
my_linkedlist.append(16)

my_linkedlist.print()
