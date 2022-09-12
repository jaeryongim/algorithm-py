"""
https://leetcode.com/problems/most-common-word/
"""
import re
from collections import Counter
from typing import List


def run(strs: str, banned: List[str]) -> str:
    words = [word for word in re.sub('[^\w]', ' ', strs).lower().split() if word not in banned]
    return Counter(words).most_common(1)[0][0]

# strs = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
strs = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
print(run(strs, banned))
