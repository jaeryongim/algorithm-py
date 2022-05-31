"""
토마토
https://www.acmicpc.net/problem/7576
"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
if n < 2 or n > 1000 or m < 2 or m > 1000:
    exit(1)

matrix = [[i for i in map(int, sys.stdin.readline().split())] for _ in range(m)]

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque()
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for e in range(4):
            _x = x + dxy[e][0]
            _y = y + dxy[e][1]
            if 0 <= _x < m and 0 <= _y < n:
                if matrix[_x][_y] == 0:
                    matrix[_x][_y] = matrix[x][y] + 1
                    queue.append((_x, _y))


bfs()
result = 0
for x in range(m):
    for y in range(n):
        if matrix[x][y] == 0:
            print(-1)
            exit(0)
    result = max(result, max(matrix[x]))

print(result - 1)
