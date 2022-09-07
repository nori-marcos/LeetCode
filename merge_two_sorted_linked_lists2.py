def merge_sorted(self, llist):
    # p e q apontam respetivamente para os seus heads
    # que possuem os menores valores das listas
    p = self.head
    q = llist.head
    # s é a nova lista que será formada, combinando os dois
    s = None

    # se p é vazio, retorna q
    if not p:
        return q
    # se q é vazio, retorna p
    if not q:
        return p

    # aqui vamos analisar quem será o head da lista s
    # de forma mais simples, quem será o primeiro item da lista s
    # primeiro, devemoos ter certeza de que se p e q não são nulos
    if p and q:
        # se o .data de p é menor que o .data de q
        # s retém o node p
        # p deve ser atualizado para o .next de s
        if p.data <= q.data:
            s = p
            p = s.next
        # caso contrário, s salva o q
        # q é atualizado com o .next de s
        else:
            s = q
            q = s.next
        # depois de decidir quem é o menor, setamos ele como nosso head da lista s
        new_head = s

    # agora começamos uma interação para organizar os nodes
    while p and q:
        if p.data <= q.data:
            s.next = p
            s = p
            p = s.next
        else:
            s.next = q
            s = q
            q = s.next
    if not p:
        s.next = q
    if not q:
        s.next = p

    self.head = new_head
    return self.head
