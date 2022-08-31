"""
https://leetcode.com/problems/reverse-string/
"""
from typing import List


def reverse_str_1(s: List[str]) -> None:
    s.reverse()
    print(s)


def reverse_str_2(s: List[str]) -> None:
    l = len(s) / 2
    i = 0
    while i < l:
        i_ = (i + 1) * -1
        p1, p2 = s[i], s[i_]
        s[i], s[i_] = p2, p1
        i+=1
    print(s)


def reverse_str_3(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)


class Solution:
    pass


reverse_str_1(["h", "e", "l", "l", "o"])
reverse_str_2(["h", "e", "l", "l", "o"])
reverse_str_3(["h", "e", "l", "l", "o"])
