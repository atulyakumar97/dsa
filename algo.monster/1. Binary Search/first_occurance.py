from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    boundary = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            boundary = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return boundary


if __name__ == '__main__':
    arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
    target = 3
    res = find_first_occurrence(arr, target)
    print(res)
