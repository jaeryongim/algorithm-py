"""
https://leetcode.com/problems/reorder-data-in-log-files/
"""
from typing import List


def reorder_log_files(logs: List[str]) -> List[str]:
    letter = []
    digit = []
    for log in logs:
        split_ = log.split()[1]
        if split_.isdigit():
            digit.append(log)
        else:
            letter.append(log)

    letter.sort(key=lambda x: (x.split()[1:], x.split()[0:]))
    return letter + digit


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(reorder_log_files(logs))
