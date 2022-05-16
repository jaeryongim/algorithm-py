"""
페어의 노드 스왑
연결 리스트를 입력받아 페어(pair) 단위로 스왑하라.

example)
input  -> 1 -> 2 -> 3 -> 4
output -> 2 -> 1 -> 4 -> 3
"""
from python_algorithm_interview.list_node import ListNode


# 단순 값의 교환
def swap_pairs_using_value(head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head



head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
swap_pairs_using_value(head)
