# to remove the last element


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

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value

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
my_linkedlist.append(9)
my_linkedlist.print()

my_linkedlist.pop()
my_linkedlist.pop()
my_linkedlist.pop()
my_linkedlist.print()
