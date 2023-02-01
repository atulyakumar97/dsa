from collections import deque


def rotate_left_till_zero(queue: deque) -> deque:
    """
    takes an integer array containing one 0
    and rotates the array counterclockwise
    so that the 0 ends up at the front
    of the array.
    """

    while queue[0] != 0:
        queue.append(queue.popleft())

    return queue


if __name__ == '__main__':
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    q.append(0)
    print(rotate_left_till_zero(q))
