def remove_duplicates(self):
    # o cur começa do self head
    cur = self.head
    # prev servirá para manter os registros da cur que será deletada
    prev = None
    # as duplicatas serão armazenadas em um hash table
    dup_values = dict()

    while cur is not None:
        if cur.data in dup_values:
            # delete o node
            prev.next = cur.next
            cur = None
        else:
            # O valor não foi encontrado anteriormente, por isso, é adicionado no dicionário
            dup_values[cur.data] = 1
            prev = cur
        cur = prev.next
