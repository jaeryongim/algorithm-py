"""
팰린드롬(Palindrome) 우리나라 말로는 "화문" 이라 부르고,
앞뒤가 똑같은 단어나 문장을 말한다.
ex) abcDcba / level / eye
"""

import collections
import re
from typing import Deque


def is_palindrome(source: str) -> bool:
    target: Deque = collections.deque()
    for e in source:
        if e.isalnum():
            target.append(e.lower())
        else:
            raise ValueError(f"{e} is invalid value")

    while len(target) > 1:
        if target.popleft(0) != target.pop():
            return False

    return True


try:
    print(is_palindrome("eye"))
except Exception as e:
    print(e)
