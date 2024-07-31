from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):
    count = 1
    queue = deque([[x, y, count]])
    while queue:
        vx, vy, count = queue.popleft()
        if vx == n - 1 and vy ==  m - 1:
            break
        for step in steps:
            if 0 <= vx + step[0] < n and 0 <= vy + step[1] < m:
                queue.append([vx + step[0], vy + step[1], count + 1])

    return count


print(bfs(0, 0))


# -------------------------book answer -----------------------------
from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
