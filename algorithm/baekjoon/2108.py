import sys

sys.stdin = open("input.txt", "r")

from collections import Counter

N = int(input())
integers = sorted([int(input()) for x in range(N)])

print(round(sum(integers) / len(integers)))

print(integers[len(integers) // 2])

counter = Counter(integers)

if len(integers) > 1 and counter.most_common()[0][1] == counter.most_common()[1][1]:
    print(counter.most_common()[1][0])
else:
    print(counter.most_common()[0][0])

print(max(integers) - min(integers))
