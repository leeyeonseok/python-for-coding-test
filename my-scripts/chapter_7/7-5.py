n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for i in range(m):
    if binary_search(N, M[i], 0, n - 1) is None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
