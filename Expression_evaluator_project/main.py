# precedence check
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

# infix to postfix
def infix_to_postfix(expression):
    stack = []
    postfix = []

    for ch in expression:
        if ch.isdigit():
            postfix.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

        else:  # operator
            while stack and precedence(stack[-1]) >= precedence(ch):
                postfix.append(stack.pop())
            stack.append(ch)

    while stack:
        postfix.append(stack.pop())

    return postfix


# evaluate postfix
def evaluate_postfix(postfix):
    stack = []

    for ch in postfix:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)

    return stack[0]


# main program
expression = input("Enter expression: ").replace(" ", "")

postfix = infix_to_postfix(expression)
print("Postfix:", " ".join(postfix))

result = evaluate_postfix(postfix)
print("Result:", result)