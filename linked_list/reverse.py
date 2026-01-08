# reversing a linked list
# most important in interview
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

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linkedlist = LinkedList(1)

my_linkedlist.append(2)
my_linkedlist.append(3)
my_linkedlist.append(4)

my_linkedlist.print()
my_linkedlist.reverse()
my_linkedlist.print()
