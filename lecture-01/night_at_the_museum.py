name = input()
count = 0
if len(name) == 0:
    print(0)
else:
    previous_letter = 'a'
    for i in range(len(name)):
        distance = abs(ord(name[i]) - ord(previous_letter))
        count += distance if distance <= (26 - distance) else (26 - distance)
        previous_letter = name[i]
    print(count)
