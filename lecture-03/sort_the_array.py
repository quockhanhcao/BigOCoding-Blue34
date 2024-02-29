n = int(input())
array = [int(num) for num in input().split()]
start_index = -1
end_index = -1

def list_reverse(arr,size):
	#if only one element present, then return the array
	if(size==1):
		return arr
	#if only two elements present, then swap both the numbers.
	elif(size==2):
		arr[0],arr[1],=arr[1],arr[0]
		return arr
	#if more than two elements presents, then swap first and last numbers.
	else:
		i=0
		while(i<size//2):
	#swap present and preceding numbers at time and jump to second element after swap
			arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
	#skip if present and preceding numbers indexes are same
			if((i!=i+1 and size-i-1 != size-i-2) and (i!=size-i-2 and size-i-1!=i+1)):
				arr[i+1],arr[size-i-2]=arr[size-i-2],arr[i+1]
			i+=2
		return arr

for i in range(n - 1):
    if(array[i] > array[i+1]):
        start_index = i
        break

for i in range(n - 1, 0, -1):
    if (start_index != -1):
        if (array[i] - array[start_index] < 0):
            end_index = i
            break
    else:
        break



if (start_index == -1):
    print('yes')
    print('1 1')
else:
    reorder_list = array[:start_index] + list_reverse(array[start_index:end_index+1], len(array[start_index:end_index+1])) + array[end_index + 1:]
    array.sort()

    if (array == reorder_list):
        print('yes')
        print(str(start_index + 1) + ' ' + str(end_index + 1))
    else:
        print('no')
