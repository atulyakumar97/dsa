from typing import List


def binary_search(arr: List[int], target: int) -> int:

    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2

    while left <= right:
        print(arr[left:right+1])
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

        mid = (left + right) // 2

    return -1


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 8]
    print(arr)
    target = 7
    res = binary_search(arr, target)
    print(res)
