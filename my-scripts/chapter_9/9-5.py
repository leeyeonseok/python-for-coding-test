import sys, heapq
INPUT = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, INPUT().split())
start = c
graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

# x에서 y로 이어지는 통로, 메시지 전달 시간 z
for _ in range(1, m + 1):
    x, y, z = map(int, INPUT().split())
    graph[x].append((y, z))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

count = 0
max_dist = 0
for i in range(1, n + 1):
    if distance[i] != INF:
        count += 1
        if max_dist < distance[i]:
            max_dist = distance[i]

print(count - 1, max_dist)
