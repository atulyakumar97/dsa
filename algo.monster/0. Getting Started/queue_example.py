from collections import deque

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
pop
pop
pop
pop
"""

queue = deque()

for step in instructions.split('\n'):

    operation = step.split(' ')[0]

    if operation == 'push':
        n = step.split(' ')[1]
        queue.append(n)

    elif operation == 'peek':
        if queue:
            print(queue[0])
        else:
            print("Queue is Empty")

    elif operation == 'pop':
        if queue:
            queue.popleft()
        else:
            print("Cannot Pop. Queue is Empty")

print(queue)
