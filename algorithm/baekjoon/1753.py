import sys

sys.stdin = open('input.txt', 'r')

import heapq
from collections import defaultdict

V, E = map(int, input().split())

k = int(input())

graph = {x: defaultdict(str) for x in range(1, V + 1)}

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances


answer = dijkstra(graph, k)

for i in range(1, V+1):
    if answer[i] == float('inf'):
        print('INF')
    else:
        print(answer[i])
