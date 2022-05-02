import sys

sys.stdin = open("input.txt", "r")

L, C = map(int, input().split())
a = sorted(list(input().split()))
visited = [False for _ in range(C)]


def check(s):
    mo, ja = 0, 0
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            mo += 1
        else:
            ja += 1
    if mo < 1 or ja < 2:
        return False
    return True


def generate(chosen):
    if len(chosen) == L and check(chosen):
        print("".join(chosen))
        return
    start = a.index(chosen[-1]) + 1 if chosen else 0
    for nxt in range(start, C):
        if visited[nxt] == 0 and (nxt == 0 or a[nxt - 1] != a[nxt] or visited[nxt - 1]):
            chosen.append(a[nxt])
            visited[nxt] = True
            generate(chosen)
            chosen.pop()
            visited[nxt] = False


generate([])
