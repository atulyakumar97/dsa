from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    """
    Bubble Sort - O(N^2)
    Pass 1 - compare current element with next element / swap if required
    Pass 2 - compare current element with next element / swap if required
    list is sorted if, during a pass, no swapping occurs.
    """
    for i in range(len(unsorted_list)):
        swapped = False
        for j in range(len(unsorted_list)-1):
            print(i, j, unsorted_list)
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                swapped = True
        if not swapped:
            return unsorted_list
    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [8, 10, 1, 3, 4, 6, 9, 2, 7, 5]
    print(0, 0, unsorted_list)
    res = sort_list(unsorted_list)
    print(res)
