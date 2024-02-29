n = int(input())
array = [int(num) for num in input().split()]
frequencies = [0] * 100001

best = 0
count = 0
right = 0

for left in range(n):
    while (right < n and count <= 2):
        if (count == 2 and frequencies[array[right]] == 0):
            break
        if (frequencies[array[right]] == 0):
            count += 1

        frequencies[array[right]] += 1
        right += 1
    best = max(best, right - left)

    if (frequencies[array[left]] == 1):
        count -= 1
    frequencies[array[left]] -= 1

    if right == n - 1:
        break

print(best)
