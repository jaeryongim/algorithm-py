"""
팰린드롬 연결 리스트
연결 리스트가 팰린드롬 구조인지 판별하라

example)
input   ->  1->2
output  ->  false

input   ->  1->2->2->1
output  ->  true

"""
import collections
from typing import List, Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def palindrome_linkedlist(head: ListNode) -> bool:
    q: List = []

    if not head:
        return True

    node = head.pop()

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True

def palindrome_deque(head: ListNode) -> bool:
    q: Deque = collections.deque()

    if not head:
        return True

    node = head.pop()

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True

def palindrome_runner(head: ListNode) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        print(fast.val)
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    # return not slow 도 가능
    return not rev


a = ListNode(1)
b = ListNode(2, a)
c = ListNode(3, b)
d = ListNode(2, c)
e = ListNode(1, d)

print(palindrome_linkedlist([a, b, c, d, e]))
print(palindrome_deque([a, b, c, d, e]))
print(palindrome_runner(e))



