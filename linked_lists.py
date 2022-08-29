class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    # The first node has a head pointing
    # to a node that does not have any data
    def __init__(self):
        self.head = Node()

    # We append a new node after looping through all nodes
    # and reach the last node in the interaction
    def append(self, data):
        cur = self.head

        # Looping through all the nodes until to find a node
        # that points to None
        # in that node we will append one more node
        while cur.next is not None:
            cur = cur.next

        new_node = Node(data)
        cur.next = new_node

    def length(self):
        cur = self.head

        # Looping through all the nodes until to find a node
        # that points to None
        # for each node we find, the counter is increased by one
        counter = 0
        while cur.next is not None:
            counter += 1
            cur = cur.next
        print(counter)

    def print_list(self):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            print(cur.data)


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.print_list()
