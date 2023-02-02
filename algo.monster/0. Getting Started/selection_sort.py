import math
from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    """
    Selection Sort - O(N^2)
    select the smallest element, swap with pos 0
    select next smallest element, swap with pos 1
    """
    for i, num in enumerate(unsorted_list):
        current = select = i
        min = math.inf

        while current < len(unsorted_list):
            if unsorted_list[current] < min:
                min = unsorted_list[current]
                select = current

            current += 1

        print('min selected:', min)

        unsorted_list[i], unsorted_list[select] = unsorted_list[select], unsorted_list[i]
        print(unsorted_list)

    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [8, 10, 1, 3, 4, 6, 9, 2, 7, 5]
    res = sort_list(unsorted_list)
    print(res)
