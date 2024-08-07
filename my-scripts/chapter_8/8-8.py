n, m = map(int, input().split())
bills = []
for i in range(n):
    bills.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for i in range(2, m + 1):
    for j in bills:
        if i % j == 0:
            d[i] = min(d[i], d[i - j] + 1)

d[m] = d[m] if d[m] != 10001 else -1
print(d[m])
