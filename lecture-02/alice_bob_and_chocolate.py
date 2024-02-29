# read input for number of chocolate bars and the eating time for each bar
chocolate_bars = int(input())
eating_time = [int(num) for num in input().split()]

i = 0
j = chocolate_bars - 1
while (i <= j):
    if (eating_time[i] < eating_time[j]):
        eating_time[j] = eating_time[j] - eating_time[i]
        eating_time[i] = 0
        if (i + 1 == j):
            break
        i += 1
    elif (eating_time[i] > eating_time[j]):
        eating_time[i] = eating_time[i] - eating_time[j]
        eating_time[j] = 0
        if (j - 1 == i):
            break
        j -= 1
    else:
        eating_time[i] = eating_time[j] = 0
        if (i + 1 == j - 1):
            i += 1
            break
        elif (i + 1 > j - 1):
            break
        i += 1
        j -= 1

print(str(i + 1), str(chocolate_bars - i - 1))
