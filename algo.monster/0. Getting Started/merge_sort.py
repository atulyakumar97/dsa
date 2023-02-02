from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    """
    Merge Sort - O(Nlog(N))
    divide and conquer
    divide the array into two almost equally
    call sort fn recursively (usually another merge sort)
    merge the two sorted lists into one
    """
    n = len(unsorted_list)

    if n <= 1:
        return unsorted_list

    # calculate middle point
    m_p = n//2

    # divide the array almost equally, call sort function recursively
    l_list, r_list = sort_list(unsorted_list[:m_p]), sort_list(unsorted_list[m_p:])

    result_list = []

    l_p = r_p = 0

    while l_p < m_p or r_p < n - m_p:
        if l_p == m_p:
            result_list.append(r_list[r_p])  # left pointer reached last element, empty out right list
            r_p += 1
        elif r_p == n - m_p:
            result_list.append(l_list[l_p])  # right pointer reached last element, empty out left list
            l_p += 1
        elif l_list[l_p] < r_list[r_p]:
            result_list.append(l_list[l_p])  # left list item is smaller so add it in result list
            l_p += 1
        else:
            result_list.append(r_list[r_p])  # right list item is smaller so add it in result list
            r_p += 1

    return result_list


if __name__ == '__main__':
    unsorted_list = [8, 10, 1, 3, 4, 6, 9, 2, 7, 5]
    print(0, 0, unsorted_list)
    res = sort_list(unsorted_list)
    print(res)
