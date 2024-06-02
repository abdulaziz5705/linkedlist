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

    def insert(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


# a = Node(7)
# b = Node(1)
# c = Node(2)
# d = Node(3)
# e = Node(4)
# l_list = LinkedList()
# l_list.head = a
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# l_list.insert(b, 45)
# print(l_list.printList())

a = Node(8)
b = Node(14)
c = Node(5)
d = Node(54)
e = Node(10)
l_list = LinkedList()
l_list.head = a
a.next = b
b.next = c
c.next = d
d.next = e
l_list.insert(d, 4)
print(l_list.printList())


a = Node(6)
b = Node(1)
c = Node(5)
d = Node(48)
e = Node(10)
l_list = LinkedList()
l_list.head = a
a.next = b
b.next = c
c.next = d
d.next = e
l_list.insert(e, 55)
print(l_list.printList())


a = Node(10)
b = Node(54)
c = Node(20)
d = Node(35)
e = Node(44)
l_list = LinkedList()
l_list.head = a
a.next = b
b.next = c
c.next = d
d.next = e
l_list.insert(c, 3)
print(l_list.printList())







