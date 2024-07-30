from collections import deque
# deque는 스택과 큐의 장점을 모두 채택한 것
# 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적
# queue 라이브러리를 이용하는 것보다 더 간단
# 대부분의 코딩 테스트에서는 collections 모듈과 같은 기본 라이브러리 사용을 허용

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
