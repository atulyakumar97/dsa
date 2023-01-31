instructions = """
8
push 3
push 7
push 20
peek
pop
push 0
push 4
pop
peek
"""

stack = []

for step in instructions.split('\n'):

    operation = step.split(' ')[0]

    if operation == 'push':
        n = step.split(' ')[1]
        stack.append(int(n))
        print(step)

    elif operation == 'peek':
        # Print the top item of the stack
        print('Top of the stack:', stack[-1])

    elif operation == 'pop':
        stack.pop()
        print(step)

    else:
        pass


print('Stack:', stack)
