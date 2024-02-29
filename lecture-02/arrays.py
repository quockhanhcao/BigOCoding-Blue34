def find_sub_array():
    [n, k] = [int(num) for num in input().split()]
    array = [int(num) for num in input().split()]

    count = [0] * (10**5 + 1)
    unique = 0
    j = 0
    i = 0
    while (i <= n -1):
        if (count[array[i]] == 0):
            unique += 1
        count[array[i]] += 1

        if (unique == k):
            while (j <= i and count[array[j]] > 1):
                count[array[j]] -= 1
                j += 1
            print(str(j + 1) + ' ' + str(i + 1))
            return
        i += 1
    # else print -1 -1
    print('-1 -1')

find_sub_array()
