# Function to define operator precedence
def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0


# Function to convert infix to postfix
def infix_to_postfix(expression):
    stack = []
    postfix = []

    for char in expression:
        if char.isdigit():  # Operand
            postfix.append(char)

        elif char == '(':
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # remove '('

        else:  # Operator
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return postfix


# Function to evaluate postfix expression
def evaluate_postfix(postfix):
    stack = []

    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()

            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)

    return stack[0]


# MAIN PROGRAM
expression = input("Enter expression: ").replace(" ", "")

postfix = infix_to_postfix(expression)
print("Postfix:", " ".join(postfix))

result = evaluate_postfix(postfix)
print("Result:", result)