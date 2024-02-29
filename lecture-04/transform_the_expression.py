t = int(input())
expressions = []
for i in range(t):
    expressions.append(input())

def transform_expression(expressions):
    stack = []
    result = ''
    for i in range(len(expressions)):
        if (expressions[i] == '('):
            continue
        elif (expressions[i] == ')'):
            result = result + stack[-1]
            stack.pop()
        elif (ord(expressions[i]) >= 97 and ord(expressions[i]) <= 122):
            result = result + expressions[i]
        else:
            stack.append(expressions[i])
    print(result)

for i in range(t):
    transform_expression(expressions[i])
