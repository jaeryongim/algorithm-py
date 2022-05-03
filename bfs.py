import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().rstrip().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = matrix[y][x] = 1

visited = [False] * (n + 1)

queue = deque()
def bfs(graph, start):
    queue.append(start)
    print(queue)
    visited[start] = True
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for idx, e in enumerate(graph[x]):
            if visited[idx] is False and e == 1:
                visited[idx] = True
                queue.append(idx)


bfs(matrix, v)


