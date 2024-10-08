array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


# quick sort 단점
# -> 이미 데이터가 정렬되어 있는 경우에는 매우 느리게 동작
# 즉, 데이터가 무작위로 입력되는 경우 퀵 정렬은 빠르게 동작할 확률이 높다.
