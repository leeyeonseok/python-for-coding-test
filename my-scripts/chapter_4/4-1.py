n = int(input())
move = list(map(str, input().split()))

location = [1, 1]
for i in move:
    if i == 'R' and location[1] < n:
        location[1] += 1
    elif i == 'L' and location[1] > 1:
        location[1] -= 1
    elif i == 'U' and location[0] > 1:
        location[0] -= 1
    elif i == 'D' and location[0] < n:
        location[0] += 1
    else:
        pass

print(*location)

# ------------------------------book answer -------------------------------------
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['U', 'D', 'L', 'R']

for plan in plans:
    nx, ny = 0, 0
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

"""
Key point
    1. dx, dy, move typs 를 리스트 로써 각각 정의 하여 한 번의 반복 으로 독립적 으로 처리가 가능
    2. move_types 의 길이 만큼 반복 하여 move_types 의 요소의 갯수가 바뀌어도 (ex. 대각선) 적용 가능
"""