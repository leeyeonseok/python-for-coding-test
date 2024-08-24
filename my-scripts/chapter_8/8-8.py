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
# ---------------------------- ↑ ↑ ↑ 8-8 풀이 ↑ ↑ ↑ -------------------------------
# n = int(input())
# nodes = list(map(int, input().split()))
# del_target = int(input())
#
#
# def dfs(nodes, start, n, del_target):
#     for i in range(start, n):
#         if nodes[i] == del_target:
#             nodes[i] = -1
#             dfs(nodes, i, n, i)
#
#
# dfs(nodes, 0, n, del_target)
# total_leaf = n
# for node in set(nodes):
#     if node in range(n):
#         total_leaf -= 1
#
# print(total_leaf - 1)

# ------------------------ 1003 정답 ----------------------
# import sys
# n = int(sys.stdin.readline())
# test_case = [int(sys.stdin.readline()) for i in range(n)]
#
# for i in range(n):
#     a, b = 1, 0
#     for j in range(test_case[i]):
#         a, b = b, a + b
#     print(a, b)
# ------------------------ 1003 정답 -----------------------

# def fibonacci(x):
#     global call_0, call_1
#     if x == 0:
#         call_0 += 1
#         return 0
#     elif x == 1:
#         call_1 += 1
#         return 1
#     else:
#         return fibonacci(x - 1) + fibonacci(x - 2)
#
#
# for i in test_case:
#     fibonacci(i)
#     print(call_0, call_1)
#     call_0, call_1 = 0, 0


n = int(input())
result = [0]
count = 9

if n < 10:
    print(n)
else:
    while count < n:
        if sum(result) / len(result) == 9:
            for i in range(len(result)):
                result[i] = 0
                result.append(1)
        



        count += 1


"""
1 - 0
2 - 1 0
3 - 2 1 0
4 - 3 2 1 0
"""



