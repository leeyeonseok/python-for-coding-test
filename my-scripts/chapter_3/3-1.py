balance = int(input())

num_500 = balance // 500
num_100 = (balance - num_500 * 500) // 100
num_50 = (balance - num_500 * 500 - num_100 * 100) // 50
num_10 = (balance - num_500 * 500 - num_100 * 100 - num_50 * 50) // 10

print(num_500 + num_100 + num_50 + num_10)

# -------------------- book answer -----------------------
n = 1260
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin
    n %= coin

print(count)
