# read input from command line
number_of_people = int(input())
claws_length = [int(num) for num in input().split()]

dead_or_alive = [1] * number_of_people
for i in range(number_of_people - 1, 0, -1):
    if (claws_length[i] == 0):
        continue
    if (i - claws_length[i] < 0):
        dead_or_alive[:i] = [0] * i
    else:
        dead_or_alive[i - claws_length[i]:i] = [0] * claws_length[i]
count = 0
for i in range(number_of_people):
    if (dead_or_alive[i] == 1):
        count += 1

print(count)
