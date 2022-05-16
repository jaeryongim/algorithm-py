"""
두 수의 덧셈
역순으로 저장된 연결 리스트의 숫자를 더하라.

example)
input  -> (2 -> 4 -> 3) + (5 -> 6 -> 4)
output -> (7 -> 0 -> 8)

설명
342 + 465 = 807
"""

from typing import List
from list_node import ListNode


def reverse_list(head: ListNode) -> ListNode:
    node, prev = head, None
    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


def to_list(node: ListNode) -> List:
    list: List = []
    while node:
        list.append(node.val)
        node = node.next
    return list


def to_linked_list(list: List) -> ListNode:
    prev: ListNode = None
    for r in list:
        node = ListNode(r)
        node.next = prev
        prev = node

    return node


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    a = to_list(reverse_list(l1))
    b = to_list(reverse_list(l2))
    result = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

    return to_linked_list(str(result))


h1 = ListNode(2, ListNode(4, ListNode(3)))
h2 = ListNode(5, ListNode(6, ListNode(4)))
result = add_two_numbers(h1, h2)
while result:
    print(result.val)
    result = result.next
