n, m, k = map(lambda x: int(x), input().split())
data = list(map(lambda x: int(x), input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0
count = 0

while count < m:
    if count != 0 and count % k == 0:
        result += second
        count += 1
        continue
    result += first
    count += 1

print(result)

# ----------------------------book answer ---------------------------------

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# --------------------------- advanced answer -------------------------------
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

# 가장 큰 수가 등장 하는 횟수
count = int(m / (k + 1)) * k + m % (k + 1)

result += count * first
result += (m - count) * second

print(result)

"""
Key point
    1. sort()를 통해 가장 큰 수와 두 번째로 큰 수 찾기
    2. 가장 큰 수를 K번 더하고, 두 번째로 큰 수를 한 번 더하는 것을 반복
    
Skills
    1. 가장 큰 수, 가장 작은 수 등을 찾을 때는, 반드시 자료를 sort 하는 과정이 필요
    2. 반복 되는 수열에 대해서 파악 하면, 반복문 을 사용 하지 않고도 문제 해결 가능
"""