import sys
from collections import deque

n = int(sys.stdin.readline())
matrix = [[i for i in (map(int, sys.stdin.readline().rstrip()))] for _ in range(n)]

visited = [[0] * n for _ in range(n)]
cnt = 1
dic = dict()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i, j):
    if matrix[i][j] == 1 and visited[i][j] == 0:
        visited[i][j] = cnt
        queue = deque()
        queue.append((i, j))
        while queue:
            print(queue)
            pop = queue.popleft()
            for p in range(4):
                x = pop[0] + dx[p]
                y = pop[1] + dy[p]
                if 0 <= x < n or 0 <= y < n:
                    if matrix[x][y] == 1 and visited[x][y] == 0:
                        visited[x][y] = cnt
                        queue.append((x, y))
        return True

    return False


for x in range(n):
    for y in range(n):
        if bfs(x, y) is True:
            print("x, y", x, y)
            cnt += 1

for f in visited:
    print(f)
