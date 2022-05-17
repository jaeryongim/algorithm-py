import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = [[v for v in map(int, sys.stdin.readline().rstrip())] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs(x, y):
    if visited[x][y] == 0 and matrix[x][y] == 1:
        xy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        visited[x][y] = 1
        queue.append((x, y))
        while queue:
            pop = queue.popleft()
            for t in xy:
                base_x = pop[0]
                base_y = pop[1]
                i = base_x + t[0]
                j = base_y + t[1]
                if -1 < i < n and -1 < j < m:
                    if matrix[i][j] == 1 and visited[i][j] == 0:
                        visited[i][j] = visited[base_x][base_y] + 1
                        if i == (n - 1) and j == (m - 1):
                            return
                        queue.append((i, j))


bfs(0, 0)
print(visited[n - 1][m - 1])


