import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())

seat = [[0] * N for x in range(N)]

likedict = defaultdict(list)

result = 0

for _ in range(N * N):
    inputt = list(map(int, input().split()))
    likedict[inputt[0]] = inputt[1:]

    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1
    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0:
                likecnt = 0
                emptycnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if seat[nx][ny] in inputt:
                            likecnt += 1
                        if seat[nx][ny] == 0:
                            emptycnt += 1
                if max_like < likecnt or (max_like == likecnt and max_empty < emptycnt):
                    max_x, max_y, max_like, max_empty = i, j, likecnt, emptycnt

    seat[max_x][max_y] = inputt[0]

for i in range(N):
    for j in range(N):
        cnt = 0
        like = likedict[seat[i][j]]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if seat[nx][ny] in like:
                    cnt += 1
        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)
