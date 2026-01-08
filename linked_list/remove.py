class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linkedlist:
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
        return pre

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
            return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepop()
        if index == self.length:
            return self.pop()
        pre = self.get(index - 1)
        # temp = self.get(index) --> this is o(n)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


my_linkedlist = linkedlist(4)

my_linkedlist.append(8)
my_linkedlist.append(12)
my_linkedlist.append(16)
my_linkedlist.print()

my_linkedlist.remove(2)

my_linkedlist.print()
