class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # o head é o primeiro node, que neste caso é nulo
        self.head = None

    def print_list(self):
        # para imprimir os nodes, começamos do head, o primeiro elemento
        cur_node = self.head

        # enquando o cur_node não foi vazio, seguimos para o próximo
        # se não houver head, isso significa que não existe node, por isso, nada será impresso
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next


    def append(self, data):
        new_node = Node(data)

        # se o head estiver vazio, isso significa que nosso node é primeiro e será colocado como head
        if self.head is None:
            self.head = new_node
            return

        # por outro lado, se o head não for nulo
        # começamos o looping considerando o head como o último node
        # ele será nosso ponto de partida para seguirmos na interação
        last_node = self.head

        # se o .next do last_node não for vazio
        # significa que ele está ocupado por um node
        # e precisamos seguir até achar um node em que o .next esteja vazio, ou seja, sem node
        while last_node.next is not None:
            last_node = last_node.next

        # depois de achar, setamos o .next do último node como o new_node
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("D")

llist.print_list()
