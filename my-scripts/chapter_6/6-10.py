n = int(input())
data = []

for i in range(n):
    data.append(int(input()))

sorted_data = sorted(data)
sorted_data.reverse()

for i in range(len(sorted_data)):
    print(sorted_data[i], end=' ')


# -----------------------------book answer -------------------------------
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
