from typing import List


def remove_duplicates(arr: List[int]) -> int:
    i = 0  # slow moving
    j = 0  # fast moving

    while j < len(arr):
        if arr[i] == arr[j]:
            j += 1
        else:
            i += 1
            arr[i] = arr[j]
    return i + 1


if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 2, 2]
    res = remove_duplicates(arr)
    print(' '.join(map(str, arr[:res])))
