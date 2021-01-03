"""
가장 긴 팰린드롬 부분 문자열을 출력하라.
투포인트 슬라이딩을 이용해 문제를 해결한다.

Example)
입력 -> "babad"
출력 -> "bab" or "aba"
"""


def longest_palindromic(s: str):
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left+1 : right-1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


print(longest_palindromic("1231331"))
