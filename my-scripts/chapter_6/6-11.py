n = int(input())

array = []
for i in range(n):
    name, score = input().split()
    array.append((name, int(score)))


array = sorted(array, key=lambda student: student[1])
for i in array:
    print(i[0], end=' ')
