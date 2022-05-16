"""
배열 파티션 1
n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

example)
input  -> [1, 4, 3, 2]
output -> 4

키 포인트
n은 2가 되며, 최대 합은 4이다.
min(1, 2) + min(3, 4) = 4
"""
from typing import List


# 오름차순(ascending) 풀이 방법
def array_pair_sum_with_ascending(nums: List[int]) -> int:
    sum = 0
    pair = []
    print(nums)
    nums.sort()
    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


# 정렬된 배열의 짝수 위치 이용하기
def array_pair_sum_with_even(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


# 코드를 파이썬 다운 방식(pythonic way)으로 풀어본다
def array_pair_sum_pythonic_way(nums: List[int]) -> int:
    nums.sort()
    return sum(sorted(nums)[::2])


inputs = [1, 4, 3, 2]
print(array_pair_sum_with_ascending(inputs))
print(array_pair_sum_with_even(inputs))
print(array_pair_sum_pythonic_way(inputs))
