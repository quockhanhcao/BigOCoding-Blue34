[n, k] = [int(num) for num in input().split()]

# read list of passwords
passwords = []
for i in range(n):
    passwords.append(input())
# read correct password
correct_password = input()

shorter_passwords = 0
same_length_passwords = 0

for i in range(len(passwords)):
    if (len(passwords[i]) < len(correct_password)):
        shorter_passwords += 1
    elif (len(passwords[i]) == len(correct_password)):
        same_length_passwords += 1

best_case = shorter_passwords + 1 + ((shorter_passwords) // k) * 5
worst_case = shorter_passwords + same_length_passwords + ((shorter_passwords + same_length_passwords - 1) // k) * 5

print(str(best_case) + ' ' + str(worst_case))
