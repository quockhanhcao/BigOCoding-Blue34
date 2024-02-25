# size of 2 arrays
array_size = input()

# number of elements to get from array 1 and 2
[k, m] = [int(num) for num in input().split()]

# 2 arrays
array1 = [int(num) for num in input().split()]
array2 = [int(num) for num in input().split()]

sub_array1 = array1[:k]
sub_array2 = array2[-m:]
is_smaller = True

if (sub_array1[-1] >= sub_array2[0]):
    is_smaller = False

if (is_smaller):
    print("YES")
else:
    print("NO")
