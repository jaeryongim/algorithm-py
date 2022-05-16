"""
문자열을 뒤집는 함수 작성
example
입력 -> ["h", "e", "l", "l", "o"]
출력 -> ["o", "l", "l", "e", "h"]
"""
from typing import List, Dict


def reverse_string1(source: List[str]) -> None:
    left, right = 0, len(source) - 1
    while left < right:
        source[left], source[right] = source[right], source[left]
        left += 1
        right -= 1
    print(source)


def reverse_string2(source: List[str]) -> None:
    result = source[::-1]
    print(result)
    # source[:] = source[::-1]
    # print(source)


reverse_string1(["h", "e", "l", "l", "o"])
reverse_string2(["p", "y", "t", "h", "o", "n"])
