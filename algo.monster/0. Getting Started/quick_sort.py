# Reference: https://www.youtube.com/watch?v=9KBwdDEwal8
from typing import List


def quick_sort(arr: List, left: int, right: int) -> None:
    """
    Quick Sort - O(Nlog(N)), Worst case - O(N^2)
    Chose Pivot element
    left subarray - smaller than pivot
    right subarray - larger than pivot
    quicksort(left), quicksort(right)
    """

    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)


def partition(arr: List, left: int, right: int) -> int:

    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:

        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


if __name__ == '__main__':
    arr = [8, 10, 1, 3, 4, 6, 9, 2, 7, 5]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
