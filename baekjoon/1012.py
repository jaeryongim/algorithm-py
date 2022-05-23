"""
유기농 배추
https://www.acmicpc.net/problem/1012
"""

import sys
from collections import deque

t = int(sys.stdin.readline())
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(a, b, max_i, max_j):
    queue = deque()
    queue.append((a, b))
    while queue:
        pop = queue.popleft()
        for r in range(4):
            xx = pop[0] + dxy[r][0]
            yy = pop[1] + dxy[r][1]
            if 0 <= xx < max_i and 0 <= yy < max_j:
                if matrix[xx][yy] == 1 and visited[xx][yy] == 0:
                    visited[xx][yy] = 1
                    queue.append((xx, yy))


for tt in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    matrix = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]

    ans = [0] * t
    for s in range(k):
        i, j = map(int, sys.stdin.readline().rstrip().split())
        matrix[i][j] = 1

    cnt = 0
    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 1 and visited[x][y] == 0:
                bfs(x, y, m, n)
                cnt += 1

    ans[tt] = cnt

    print(ans[tt])
