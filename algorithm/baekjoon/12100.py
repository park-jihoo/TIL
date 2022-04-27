import sys
import copy

sys.stdin = open("input.txt", "r")

N = int(input())
a = [[int(x) for x in input().split()] for _ in range(N)]
ans = 0


def move(way):
    if way == 0:
        for j in range(N):
            idx = 0
            for i in range(1, N):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[idx][j] == 0:
                        a[idx][j] = temp
                    elif a[idx][j] == temp:
                        a[idx][j] = temp * 2
                    else:
                        idx += 1
                        a[idx][j] = temp
    if way == 1:
        for j in range(N):
            idx = N - 1
            for i in range(N - 2, -1, -1):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[idx][j] == 0:
                        a[idx][j] = temp
                    elif a[idx][j] == temp:
                        a[idx][j] = temp * 2
                    else:
                        idx -= 1
                        a[idx][j] = temp
    if way == 2:
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[i][idx] == 0:
                        a[i][j] = temp
                    elif a[i][idx] == temp:
                        a[i][idx] = temp * 2
                    else:
                        idx += 1
                        a[i][idx] = temp
    if way == 3:
        for i in range(N):
            idx = 0
            for j in range(N - 2, -1, -1):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[i][idx] == 0:
                        a[i][j] = temp
                    elif a[i][idx] == temp:
                        a[i][idx] = temp * 2
                    else:
                        idx -= 1
                        a[i][idx] = temp


def dfs(cnt):
    global a, ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, a[i][j])
        return
    temp_a = copy.deepcopy(a)
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        a = copy.deepcopy(temp_a)


dfs(0)
print(ans)
