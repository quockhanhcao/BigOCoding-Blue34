[number_of_books, free_times] = [int(num) for num in input().split()]
# reading time for every books
reading_times = [int(num) for num in input().split()]

max_read_books = 0
remaining_time = free_times
count = 0

for i in range(len(reading_times)):
    j = i
    while (j <= len(reading_times) - 1 and remaining_time >= reading_times[j]):
        remaining_time -= reading_times[j]
        count += 1
        j += 1
    else:
        remaining_time = free_times
        max_read_books = count
        count = 0

print(max_read_books)
