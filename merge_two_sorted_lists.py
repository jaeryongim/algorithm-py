"""
정렬되어 있는 두 연결 리스트를 합쳐라.

example)
input  -> 1->2->4 , 1->3->4
output -> 1->1->2->3->4->4

"정렬"이 되어 있는 리스트라는 점이 중요
"""
from list_node import ListNode


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and (l1.val > l2.val)):
        l1, l2 = l2, l1

    if l1:
        l1.next = merge_two_lists(l1.next, l2)

    return l1


a = ListNode(4)
b = ListNode(2, a)
c = ListNode(1, b)

d = ListNode(4)
e = ListNode(3, d)
f = ListNode(1, e)

result = merge_two_lists(c, f)
while result:
    print(result.val)
    result = result.next
