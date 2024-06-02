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

    def insert(self, prev_node, new_data):
        new_el = Node(new_data)
        new_el.next = prev_node.next
        prev_node.next = new_el

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


a = Node(4)
b = Node(5)
c = Node(10)
d = Node(6)
l_list = LinkedList()

l_list.head = a
a.next = b
b.next = c
c.next = d
print(f"Dastlabki holati: {l_list.printList()}")
l_list.push(5)
print(f"Kiyengi  holati: {l_list.printList()}")
