number_of_intervals = int(input())

good_timestamps = input().split()

if (number_of_intervals == 0):
    print(0)
else:
    count = 0
    previous_timestampt = 0
    for i in range(len(good_timestamps)):
        if (previous_timestampt + 15) >= int(good_timestamps[i]):
            count = 15 + int(good_timestamps[i])
            previous_timestampt = int(good_timestamps[i])
        else:
            count = 15 + previous_timestampt
            break
    print(count if count <= 90 else 90)
