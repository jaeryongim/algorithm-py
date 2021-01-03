"""
자신을 제외한 배열의 곱
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

example)
input  -> [1, 2, 3, 4]
output -> [24, 12, 8, 6]

키 포인트
나눗셈을 하지 않고 O(n)에 풀이하라.
"""
import math
from typing import List


def base_solving(nums: List[int]) -> List[int]:
    # 나눗셈을 하지 않고 풀라는 문제의 조건
    result = []
    total = math.prod(nums)
    for n in nums:
        result.append(int(total/n))

    return result


def product_except_self(nums: List[int]) -> List[int]:
    p = 1
    out = []
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    for i in range(len(nums) - 1, -1, -1):
        print('i > ', i)
        out[i] = out[i] * p
        p = p * nums[i]
    return out


print(base_solving([1, 2, 3, 4]))
print('-------------------')
print(product_except_self([1, 2, 3, 4]))
