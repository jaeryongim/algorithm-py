import sys
from collections import deque

n = int(sys.stdin.readline())
if n < 5 or n > 25:
    exit(1)

matrix = [[i for i in (map(int, sys.stdin.readline().rstrip()))] for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dic = dict()
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 1


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    if matrix[i][j] == 1 and visited[i][j] == 0:
        visited[i][j] = cnt
        while queue:
            pop = queue.popleft()
            for p in range(4):
                x = pop[0] + dxy[p][0]
                y = pop[1] + dxy[p][1]
                if 0 <= x < n and 0 <= y < n:
                    if matrix[x][y] == 1 and visited[x][y] == 0:
                        visited[x][y] = cnt
                        v = dic.get(cnt, 0)
                        v += 1
                        dic[cnt] = v
                        queue.append((x, y))
        return True
    return False


for x in range(n):
    for y in range(n):
        if matrix[x][y] == 1 and visited[x][y] == 0:
            bfs(x, y)
            cnt += 1

arr = [0 for _ in range(cnt)]
for x in range(n):
    for y in range(n):
        if visited[x][y] != 0:
            arr[visited[x][y]] += 1

arr.sort()
print(cnt - 1)
for x in range(len(arr)):
    if x != 0:
        print(arr[x])

for x in range(7):
    print(visited[x])

# 7
# 0110101
# 0110100
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
