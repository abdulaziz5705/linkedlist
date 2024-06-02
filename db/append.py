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

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


# a = Node(10)
# b = Node(54)
# c = Node(20)
# d = Node(35)
# e = Node(44)
# l_list = LinkedList()
# l_list.head = a
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# l_list.append(5)
# print(l_list.printList())
#
# a = Node(8)
# b = Node(4)
# c = Node(2)
# d = Node(3)
# e = Node(4)
# l_list = LinkedList()
# l_list.head = a
# a.next = b
# b.next = d
# d.next = c
# c.next = e
# l_list.append(4)
# print(l_list.printList())

# a = Node(5)
# b = Node(9)
# c = Node(2)
# d = Node(5)
# e = Node(4)
# l_list = LinkedList()
# l_list.head = a
# a.next = b
# b.next = d
# d.next = e
# e.next = c
# l_list.append(1)
# print(l_list.printList())

a = Node(5)
b = Node(89)
c = Node(78)
d = Node(3)
e = Node(4)
l_list = LinkedList()
l_list.head = a
a.next = b
b.next = c
c.next = d
d.next = e
l_list.append(100)
print(l_list.printList())
