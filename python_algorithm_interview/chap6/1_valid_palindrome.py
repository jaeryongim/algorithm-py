"""
https://leetcode.com/problems/valid-palindrome/
"""
import sys
from collections import deque


class Solution:
    def is_palindrome_1(self, strs) -> bool:
        # 풀이1
        list = []
        flag = True
        for c in strs:
            if c.isalnum():
                list.append(c.lower())

        l = len(list)
        for idx in range(0, int(l / 2)):
            front = list[idx]
            back = list[l - 1 - idx]
            if front != back:
                flag = False

        return flag

    def is_palindrome_2(strs) -> bool:
        # 풀이2
        d = deque()
        for c in strs:
            if c.isalnum():
                d.append(c.lower())

        print(d[::-1])
        while len(d) > 1:
            if d.popleft() != d.pop():
                return False
        return True


solution = Solution().is_palindrome_2(sys.stdin.readline().rstrip())
print(solution)


