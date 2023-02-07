from typing import List


def first_not_smaller(arr: List[int], target: int) -> int:

    left = 0
    right = len(arr) - 1
    boundary = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:  # if true, reject right array
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary


if __name__ == '__main__':
    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6
    res = first_not_smaller(arr, target)
    print(res)
