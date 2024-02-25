number_of_buttons = input()
buttoned_order = input().split()

if len(number_of_buttons) == 1:
    if (buttoned_order[0] == '1'):
        print("YES")
    else:
        print("NO")
else:
    count = 0
    for i in range(len(buttoned_order)):
        if (buttoned_order[i] == '0'):
            count = count + 1
    if count != 1:
        print("NO")
    else:
        print("YES")
