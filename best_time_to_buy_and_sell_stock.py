"""
주식을 살고팔기 가장 좋은 시점
한 번의 거래로낼 수 있는 최대 이익을 산출하라.

example)
input  -> [7, 1, 5, 3, 6, 4]
output -> 5

키 포인트
1일 때 사서 6일 때 팔면 5의 이익을 얻는다.
"""
import sys
from typing import List

# brute force
def max_profit_brute_force(prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i + 1, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

def max_profit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for i, price in enumerate(prices):
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit_brute_force([7, 1, 5, 3, 6, 4]))
