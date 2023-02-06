def square_root(n: int) -> int:
    if n == 0:
        return 0

    left = 0
    right = n
    boundary = -1

    while left <= right:

        mid = (left + right) // 2

        if mid * mid == n:
            return mid
        elif mid * mid < n:
            left = mid + 1
        else:
            boundary = mid
            right = mid - 1

    return boundary - 1


if __name__ == '__main__':
    n = 16
    res = square_root(n)
    print(res)
