from typing import List


def two_pointer(n: int, arr: List[int]) -> int:
    result = 0
    sum = 0
    end = 0
    for start, _ in enumerate(arr):
        while sum < n and end < len(arr):
            sum += arr[end]
            end += 1

        if sum == n:
            result += 1

        sum -= arr[start]

    return result

print(two_pointer(5, [1, 2, 3, 2, 5]))
