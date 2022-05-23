"""
바이러스
https://www.acmicpc.net/problem/2606
"""
import sys
from collections import deque

computer_count = int(sys.stdin.readline())
if computer_count > 100:
    exit(1)

matrix = [[] for _ in range(computer_count + 1)]
pair_count = int(sys.stdin.readline())

for _ in range(pair_count):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x].append(y)
    matrix[y].append(x)

visited = [False] * (computer_count + 1)

def bfs():
    result = 0
    queue = deque()
    queue.append(1)
    visited[1] = True
    while queue:
        pop = queue.popleft()
        for computer in matrix[pop]:
            if visited[computer] is False:
                queue.append(computer)
                visited[computer] = True
                result += 1
    return result


print(bfs())
