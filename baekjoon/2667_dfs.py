"""
단지번호 붙이기
https://www.acmicpc.net/problem/2667
"""

import sys
n = int(sys.stdin.readline())
matrix = [[i for i in (map(int, sys.stdin.readline().rstrip()))] for _ in range(n)]

visited = [[0] * n for _ in range(n)]
cnt = 1
d = dict()

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        return False

    if matrix[i][j] == 1 and visited[i][j] == 0:
        visited[i][j] = cnt
        v = d.get(cnt, 0)
        v += 1
        d[cnt] = v
        dfs(i-1, j)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i, j+1)
        return True
    return False


for x in range(n):
    for y in range(n):
        if dfs(x, y) is True:
            cnt += 1


eachComplexCnt = list(d.values())
eachComplexCnt.sort()

print(cnt - 1)
for c in eachComplexCnt:
    print(c)
