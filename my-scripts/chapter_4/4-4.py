# 맵의 크기 입력
n, m = map(int, input().split())
sim_map = [[0 for _ in range(m)] for _ in range(n)]

# 초기 위치와 heading 입력
ix, iy, heading = map(int, input().split())
move_type = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 맵의 크기에 맞는 지도 입력
for i in range(n):
    sim_map[i] = list(map(int, input().split()))

# 이동 과정 작성
cur_x, cur_y = ix, iy
result, count = 1, 0

while True:
    if sim_map[cur_x + move_type[heading][0]][cur_y + move_type[heading][1]] == 0:
        sim_map[cur_x][cur_y] = 1
        cur_x += move_type[heading][0]
        cur_y += move_type[heading][1]
        result += 1
        count = 0
    else:
        heading = (heading + 3) % 4
        count += 1
        if count > 4:
            break

# 출력
print(result)

# def print_grid(grid):
#     for i in range(len(sim_map)):
#         for j in  range(len(sim_map[0])):
#            print(sim_map[i][j], end=' ')
#         print()
#     print()
#
# print_grid(sim_map)

# ---------------------------- book answer --------------------------------
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1 ,0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1