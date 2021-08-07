class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    current = node
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()


node1 = Node("A")
print(node1.data)

# A -> Ø


node2 = Node("B")
node3 = Node("C")
node1.next = node2
node2.next = node3

print_list(node1)