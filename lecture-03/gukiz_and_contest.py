n = int(input())
scores = [int(num) for num in input().split()]

frequencies = [0] * 2001

for i in range(n):
    frequencies[scores[i]] += 1

orders = {}
previous_score = 0
for i in range(2000, -1, -1):
    if (frequencies[i] != 0):
        orders[i] = 1 + previous_score
        previous_score += frequencies[i]

result = ''
for i in range(n):
    result += str(orders[scores[i]]) + ' '

print(result)
