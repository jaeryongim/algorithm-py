"""
연결 리스트를 뒤집어라.
https://leetcode.com/problems/reverse-linked-list/
입력 -> 1 -> 2 -> 3 -> 4 -> 5 -> NULL
출력 -> 5 -> 4 -> 3 -> 2 -> 1 -> NULL
"""
from python_algorithm_interview.list_node import ListNode


def reverse_list_recursion(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev

        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)

def reverse_list_while(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# result = reverse_list_recursion(node)
result = reverse_list_while(node)


