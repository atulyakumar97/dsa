from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    """
    Basic Sort - O(N^2)
    Compare current element with next element
    """
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list)-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [8, 10, 1, 3, 4, 6, 9, 2, 7, 5]
    res = sort_list(unsorted_list)
    print(res)
