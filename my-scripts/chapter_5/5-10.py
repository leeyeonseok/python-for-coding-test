# 얼음 틀 입력
# n, m = map(int, input().split())
#
# data = [[0 for _ in range(m)] for _ in range(n)]
# for i in range(n):
#     data[i] = list(map(int, input().split()))
#
# # 인접 리스트 활용 인접 개수 계산
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# steps = ['북', '남', '서', '동']
# visited = [[0 for _ in range(m)] for _ in range(n)]
#
#
# def dfs(graph, visited):
#
#
#
#
# def search_start(graph, visited):
#     for i in range(len(n * m)):
#         if graph[i // m][i % m] == 0:
#             return i // m, i % m
#     return -1
#
#
# vx, vy = search_start(data, visited) if search_start(data, visited) != -1 else -1, -1

# 출력

# def print_grid(grid):
#     for i in grid:
#         for j in i:
#             print(j, end=' ')
#         print()
#     print()
#
#
# print_grid(data)


# ------------------------book answer -------------------------------
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) is True:
            result += 1

print(result)  # 정답 출력
