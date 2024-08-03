n, k = map(int, input().split())
data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

data1.sort()
data2.sort()

for i in range(k):
    if data1[i] < data2[n - i - 1]:
        data1[i], data2[n - i - 1] = data2[n - i - 1], data1[i]
    else:
        break

print(sum(data1))


# -------------------------book answer ------------------------------
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True)  # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최댛 K번 비교
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
