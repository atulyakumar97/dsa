from typing import List


def find_min_rotated(arr: List[int]) -> int:
    if len(arr) == 1:
        return 0

    left = 0
    right = len(arr) - 1
    boundary = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= arr[-1]:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary


if __name__ == '__main__':
    arr = [3, 5, 7, 11, 13, 17, 19, 2]
    res = find_min_rotated(arr)
    print(res)
