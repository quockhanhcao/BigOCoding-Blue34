n = int(input())
lengths = [int(num) for num in input().split()]

# lengths.sort()

max_height = 0
number_of_towers = 0
unique = [0] * 1001

for i in range(n):
    if (unique[lengths[i]] == 0):
        number_of_towers += 1
    unique[lengths[i]] += 1
    max_height = max(max_height, unique[lengths[i]])

print(str(max_height) + ' ' + str(number_of_towers))
