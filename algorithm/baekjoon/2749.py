import sys

sys.stdin = open("input.txt", "r")
N = int(input())

lists = [0, 1, 1]

for i in range(3, N+1):
    lists[i%3] = (lists[(i+1)%3] + lists[(i+2)%3])

print(lists[i%3])