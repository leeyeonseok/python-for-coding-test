n, k = map(int, input().split())
count = 0

while n > 1:
    n = n // k if n % k == 0 else n - 1
    count += 1

print(count)

# -------------------book answer -----------------------------
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

# ---------------------------- advanced answer --------------------------
# 만약 N이 100억 이상의 큰 수가 되는 경우를 가정 했을 때 빠르게 동작 하려면?
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
print(result)
