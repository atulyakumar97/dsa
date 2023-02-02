from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    """
    Insertion sort - O(N^2)
    Consider first item of the array sorted
    Compare Element 2 with Element 1 swap if smaller
    Compare Element 3 compare with element 2 swap if smaller,
         ...Compare Element 2 with Element 1 swap if smaller
    """

    for i, entry in enumerate(unsorted_list):
        current = i

        while current > 0 and unsorted_list[current] < unsorted_list[current-1]:
            unsorted_list[current-1], unsorted_list[current] = unsorted_list[current], unsorted_list[current-1]
            current -= 1

        print(unsorted_list)
    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [8, 10, 1, 3, 4, 6, 9, 2, 7, 5]
    res = sort_list(unsorted_list)
    print(res)

