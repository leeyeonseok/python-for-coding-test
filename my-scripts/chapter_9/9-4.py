import sys

INPUT = sys.stdin.readline
INF = int(1e9)

n, m = map(int, INPUT().split())

graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(1, m + 1):
    a, b = map(int, INPUT().split())
    graph[a][b], graph[b][a] = 1, 1

x, k = map(int, INPUT().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)
