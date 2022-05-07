import re
from collections import Counter


def remove_duplicates(s: str, k: int) -> str:
    size = len(s)
    if k > size or not k:
        return s
    stack = []
    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
            continue
        stack.append([c, 1])
    ans = ''
    for value, count in stack:
        ans += value * count
    return ans


if __name__ == '__main__':
    print(remove_duplicates("pbbcggttciiippooaais", 2))
