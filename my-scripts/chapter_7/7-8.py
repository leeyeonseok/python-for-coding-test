n, m = map(int, input().split())
input_list = list(map(int, input().split()))
length = sum(input_list)
height = 0

while True:
    for i in range(len(input_list)):
        if input_list[i] > 0:
            input_list[i] -= 1
            length -= 1
    height += 1

    if length == m:
        break
    elif length < m:
        height -= 1
        break
    else:
        pass

print(height)
# 시간 초과 X X X X X X X X X X X X

# ------------------------my advanced answer ----------------------------
n, m = map(int, input().split())
input_list = list(map(int, input().split()))
max_length = max(input_list)


def binary_search(target, start, end):
    while True:
        total_length = 0
        mid = (start + end) // 2
        for i in range(len(input_list)):
            if input_list[i] - mid < 0:
                total_length += 0
            else:
                total_length += input_list[i] - mid
        if total_length == target:
            break
        elif total_length > target:
            start = mid + 1
        else:
            end = mid - 1
    return mid

print(binary_search(m, 0, max_length))


# ------------------------- book answer --------------------------
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
