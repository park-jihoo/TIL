import sys

sys.stdin = open("input.txt", "r")

N, L = map(int, input().split())

board = [[int(x) for x in input().split()] for _ in range(N)]

slope = [[0] * N for _ in range(N)]

answer = 0


def check(x, y, flag):
    height = [0] * (N + 1)
    visit = [False] * (N + 1)

    for i in range(N):
        if flag == 0:
            height[i] = board[x][i]
        else:
            height[i] = board[i][y]

    for i in range(N - 1):
        if height[i] == height[i + 1]:
            continue
        elif height[i] - 1 == height[i + 1]:
            for j in range(i + 1, i + 1 + L):
                if j > N:
                    return False
                if visit[j]:
                    return False
                if height[i + 1] != height[j]:
                    return False
                visit[j] = True
        elif height[i] + 1 == height[i + 1]:
            for j in range(i, i - L, -1):
                print(i, i-L, j)
                if j < 1:
                    return False
                if visit[j]:
                    return False
                if height[i] != height[j]:
                    return False
                visit[j] = True
        else:
            return False
    return True


for i in range(N):
    answer += check(i, 0, 0)
    answer += check(0, i, 1)

print(answer)
