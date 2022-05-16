"""
상하좌우 문제
greedy 문제 풀이
"""
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
# dic = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

for plan in plans:
    # map으로 LRUD와 좌표를 초기화 하는 방법도 가능
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)

