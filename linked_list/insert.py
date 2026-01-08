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
        return True

    def prepend(self, value):
        first_node = Node(value)
        if self.head is None:
            self.head = first_node
            self.tail = first_node

        else:
            first_node.next = self.head
            self.head = first_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


my_linkedlist = linkedlist(4)

my_linkedlist.append(8)
my_linkedlist.append(12)
my_linkedlist.append(16)
my_linkedlist.print()

my_linkedlist.insert(1, 23)

my_linkedlist.print()
