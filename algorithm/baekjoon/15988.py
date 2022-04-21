import sys

sys.stdin = open("input.txt", "r")

T = int(input())
ans = [0, 1, 2, 4]
for i in range(T):
    n = int(input())
    if n <= len(ans) - 1:
        print(ans[n])
    else:
        for i in range(len(ans), n+1):
            ans.append(ans[i-3]+ans[i-2]+ans[i-1])
        print(ans[n])