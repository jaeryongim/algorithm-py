"""
그룹 애너그램
문자열 배열을 받아 애너그램 단위로 그룹핑하라.

example)
input  -> ["eat", "tea", "tan", "ate", "nat", "bat"]
output ->
[
  ["ate", "eat", "tea"],
  ["nat", "tan"],
  ["bat"]
]

키 포인트
1. python의 dictionary는 key:value 해시 테이블 자료형 임을 아는 것
2. KeyError를 막기 위한 defaultdict을 사용하는 것
"""
import collections
from typing import List

inputs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()


print(group_anagrams(inputs))

