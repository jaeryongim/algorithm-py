"""
곱하기 혹은 더하기
greedy 문제 풀이
"""

input = '02984'
result = 0
for e in input:
    num = int(e)
    if num < 2 or result < 2:
        result += num
    else:
        result *= num

print('result > ', result)
