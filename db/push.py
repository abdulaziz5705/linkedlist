class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


# a = Node(4)
# b = Node(5)
# c = Node(14)
# d = Node(7)
# e = Node(10)
# l_l = LinkedList()
# l_l.head = a
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# l_l.push(56)
# print(l_l.printList())

# a = Node(1)
# b = Node(8)
# c = Node(4)
# d = Node(7)
# e = Node(0)
# l_l = LinkedList()
# l_l.head = a
# a.next = b
# b.next = c
# c.next = e
# e.next = d
# l_l.push(20)
# print(l_l.printList())

# a = Node(4)
# b = Node(5)
# c = Node(14)
# d = Node(7)
# e = Node(10)
# l_l = LinkedList()
# l_l.head = a
# a.next = b
# b.next = d
# d.next = c
# e.next = c
# l_l.push(36)
# print(l_l.printList())

# a = Node(0)
# b = Node(1)
# c = Node(2)
# d = Node(7)
# e = Node(10)
# l_l = LinkedList()
# l_l.head = a
# a.next = c
# c.next = b
# b.next = d
# d.next = e
# l_l.push(5)
# print(l_l.printList())

a = Node(6)
b = Node(87)
c = Node(1)
d = Node(7)
e = Node(65)
l_l = LinkedList()
l_l.head = a
a.next = b
b.next = e
e.next = d
d.next = c
l_l.push(65)
print(l_l.printList())