import sys
from time import time

sys.stdin = open("input.txt", "r")
N = int(input())
classes = [int(x) for x in input().split()]
B, C = map(int, input().split())

answer = 0

for i in classes:
    if i <= B:
        answer += 1
    else:
        answer += 1
        answer += ((i - B - 1) // C) + 1

print(answer)
