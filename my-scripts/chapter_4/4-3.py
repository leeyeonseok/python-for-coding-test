# 입력을 row col 로 분리
input_data = input()
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
init_pos_c = row.index(input_data[0]) + 1
init_pos_r = int(input_data[1])
count = 0

# 이동 가능한 경우 찾기
dx = [-1, 1, -1, 1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, -1, 1, -1, 1]

for i in range(8):
    nx = init_pos_r + dx[i]
    ny = init_pos_c + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

# 출력
print(count)
