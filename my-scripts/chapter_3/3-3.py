row, col = map(int, input().split())
data = []
for _ in range(row):
    input_data = list(map(int, input().split()))
    data.append(sorted(input_data))

max_val = 0

for i in range(row):
    if data[i][0] > max_val:
        max_val = data[i][0]

print(max_val)

# ---------------------------------book answer -----------------------------------
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

"""
Key point
    1. 최댓값 or 최솟값을 찾을 땐 min, max 내장 함수 사용
    2. 될 수 있으면 반복을 여러 번 하지 않고 한 번의 반복에 끝내기
"""