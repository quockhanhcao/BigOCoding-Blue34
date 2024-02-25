s = input()
t = input()

letter_count_s = [0] * 26
letter_count_t = [0] * 26
for i in range(len(s)):
    letter_count_s[ord(s[i]) - 97] += 1

for j in range(len(t)):
    letter_count_t[ord(t[j]) - 97] += 1

is_array = False
is_automaton = False
is_need_tree = False
matching_position = -1
length_t = len(t)
length_s = len(s)

for i in range(26):
    if (letter_count_t[i] > letter_count_s[i]):
        is_need_tree = True
    elif (letter_count_t[i] < letter_count_s[i]):
        is_automaton = True

for i in range(length_t):
    matching_position = s.find(t[i], matching_position + 1)
    if matching_position == -1:
        is_array = True
        break


if (is_need_tree):
    print('need tree')
elif (is_automaton and is_array):
    print('both')
elif (is_automaton):
    print('automaton')
else:
    print('array')
