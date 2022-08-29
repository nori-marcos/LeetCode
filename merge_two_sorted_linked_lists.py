# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    head = dummy

    # enquanto o elemento da lista 1 e da lista 2 não forem nulos, faça a seguinte repetição
    while list1 is not None and list2 is not None:

        if list1.val < list2.val:

            # o próximo elemento da nossa lista dummy (dummy.next) será o head da lista 1
            dummy.next = list1

            # o head da lista1 vai para o seguinte elemento (list1.next)
            list1 = list1.next

        else:

            # o próximo elemento da nossa lista dummy (dummy.next) será o head da lista 2
            dummy.next = list2

            # o head da lista2 vai para o seguinte elemento (list2.next)
            list2 = list2.next

        # o dummy também precisa ser atualizado para ser o dummy.next, que às vezes pode ser da lista 1 ou da lista 2
        dummy = dummy.next

    # se a lista 1 ainda não acabou
    if list1 is not None:
        dummy.next = list1

    # se a lista2 ainda não acabou
    else:
        dummy.next = list2

    # retorna o head de onde toda a lista dummy começou
    return head.next
