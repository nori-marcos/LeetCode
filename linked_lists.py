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
            print(f"The head is empty, so the node {new_node.data} will be the new head.")
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

    def insert_after_node(self, prev_node, data):
        # se não existir o node indicado ou pedido, apenas dizer que ele não existe
        if not prev_node:
            print("Previous node does not exist.")
            return

        # caso exista, crie um novo node com a informação solicitada
        new_node = Node(data)

        # coloque o node novo antes do node a ser antecipado
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        # aqui setamos o cur_node como self_head para começarmos o nosso traverse pelo linked list
        cur_node = self.head

        # para o caso em que tivermos que deletar o head
        # precisamos saber que o cur_node (o head) não é nulo
        # e as informação da chave de ser a mesma do .data do head
        if cur_node is not None and cur_node.data == key:
            # aqui atualizamos o head para ser o node que vem depois do head anterior
            self.head = cur_node.next
            # depois de setar o head para o próximo,
            # deletamos a informação setando a informação para None
            cur_node = None
            return

        # agora partimos para a deleção de nodes que não são o head
        # marcamos um prev com None, que marcará o node anterior ao que será deletado
        prev = None

        # enquanto o cur_node não for nulo e o .data do cur_node não corresponder a chave
        while cur_node is not None and cur_node.data != key:
            # o prev vai ficar guardando a posição do cur_node que antecede ao que será deletado
            prev = cur_node
            # cur_node vai se atualizando para ser o próximo da lista
            cur_node = cur_node.next

        # quando o cur_node for nulo, significa que a chave não existe no linked list
        if cur_node is None:
            print(f"The key {key} does not exist in the linked list.")
            return

        # se o cur_node não for nulo, a chave existe
        # então o .next do node prévio apontará para o .next do cur_node a ser deletado
        prev.next = cur_node.next
        # por fim, o cur_node é setado como nulo
        cur_node = None

    # implementação da deleção por posição
    def delete_node_at_pos(self, pos):
        if self.head is not None:
            cur_node = self.head

            # se a posição for zero, significa que o head será deletado
            if pos == 0:
                # por isso, o head é passado para o .next do head
                self.head = cur_node.next
                # head é colocado como nulo
                cur_node = None
                return

            # se a deleção for de outro node que não for no head
            prev = None
            # é feito um contador para encontrar a posição do node
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def length(self):
        cur_node = self.head

        count = 0

        while cur_node is not None:
            count += 1
            cur_node = cur_node.next

        print(count)
        return count

    def swap_nodes(self, key_1, key_2):
        # se as chaves forem iguais, nada acontece
        if key_1 == key_2:
            return

        # rastreamos a primeira chave que
        # não pode ser nula
        # seu .data deve ser igual a chave 1
        prev_1 = None
        curr_1 = self.head
        while curr_1 is not None and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        # rastreamos a segunda chave que
        # não pode ser nula
        # seu .data deve ser igual a chave 2
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        # se o head não existe, não retorna nada
        if not curr_1 or not curr_2:
            return

        # se o prev 1 não for nulo, ele deve se ligar ao curr_2
        if prev_1 is not None:
            prev_1.next = curr_2

        # caso contrário, significa que o próprio curr_2 será o head
        else:
            self.head = curr_2

        if prev_2 is not None:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        # depois de setar onde os nodes previous apontarão
        # mudamos para onde apontará o node de cada current
        # current 1 apontará para o .next do current 2
        # vice-versa
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    # inversão da lista
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur is not None:
            #  A -> B -> C -> D -> None
            # A é o head, atual cur
            # nxt será o .next de cur, ou seja, B
            # o .next de cur será atualizado para o prev, que se encontra None
            # None (prev) <- A (antigo cur e novo prev) B (novo cur e antigo nxt) -> C (novo nxt)
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # o novo head será o último node na interação que não é None, neste caso, D
        self.head = prev


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")

# llist.prepend("D")
# o node depois do head significa que é o node B que vem depois do A
llist.insert_after_node(llist.head.next, "D")

llist.print_list()

llist.length()
