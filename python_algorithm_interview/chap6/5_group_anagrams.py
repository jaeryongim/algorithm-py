"""
https://leetcode.com/problems/group-anagrams/
"""
import collections
from typing import List


def anagrams(strs: List[str]) -> List[List[str]]:
    dic = collections.defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        dic[key].append(s)

    return list(dic.values())



arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagrams(arr))
