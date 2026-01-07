# removing the first element from the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linkedlist:
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

    def append(self, value):
        first_node = Node(value)
        if self.head is None:
            self.head = first_node
            self.tail = first_node
        else:
            self.tail.next = first_node
            self.tail = first_node
        self.length += 1

    def prepop(self):

        if self.head is None:
            return None
        else:
            pre = self.head
            temp = self.head
            temp = pre
            temp = temp.next
            self.head = temp
            # (or)
            # temp = self.head
            # self.head = self.head.next
            # temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return pre.value


my_linkedlist = linkedlist(4)

my_linkedlist.append(8)
my_linkedlist.append(12)
my_linkedlist.append(16)
my_linkedlist.print()


my_linkedlist.prepop()
my_linkedlist.print()
