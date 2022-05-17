import sys

n, m, v = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = matrix[y][x] = 1

visited = [False] * (n + 1)

def dfs(graph, start):
    visited[start] = True
    print(start, end=' ')
    for idx, e in enumerate(graph[start]):
        if e == 1 and visited[idx] is False:
            dfs(graph, idx)


dfs(matrix, v)
