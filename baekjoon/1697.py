"""
숨바꼭질
https://www.acmicpc.net/problem/1697
n 수빈(순간이동, 걷거나), k 동생
수빈 위치가 5, 동생의 위치가 17일 경우
5 10 9 18 17 순으로 가면 4초만에 동생을 찾을 수 있다.
"""
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

visited = [False] * 100_001
matrix = [0] * 100_001
def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        pop = queue.popleft()
        if pop == k:
            break
        if 0 <= pop + 1 < 100_001 and visited[pop + 1] is False:
            visited[pop + 1] = True
            matrix[pop + 1] = matrix[pop] + 1
            queue.append(pop + 1)

        if 0 <= pop - 1 < 100_001 and visited[pop - 1] is False:
            visited[pop - 1] = True
            matrix[pop - 1] = matrix[pop] + 1
            queue.append(pop - 1)

        if 0 <= pop * 2 < 100_001 and visited[pop * 2] is False:
            visited[pop * 2] = True
            matrix[pop * 2] = matrix[pop] + 1
            queue.append(pop * 2)


bfs(n)
print(matrix[k])

