"""
연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""
import sys
# 최대 재귀 한도 제한 변경
sys.setrecursionlimit(99999)

n, m = map(int, sys.stdin.readline().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
visited[0] = True

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    matrix[u][v] = matrix[v][u] = 1

cnt = 0
def dfs(start):
    visited[start] = True
    for idx, value in enumerate(matrix[start]):
        if value == 1 and visited[idx] is False:
            dfs(idx)


for e in range(1, n + 1):
    if visited[e] is True:
        continue
    dfs(e)
    cnt += 1

print(cnt)

