from typing import List, Dict
from collections import Counter


def get_counter(items: List) -> Dict:
    """
    takes an integer array and returns
    a hash table with the array elements
    as keys and their frequencies as values.
    """
    counter = dict()

    for item in items:
        counter[item] = counter.get(item, 0) + 1

    return counter


if __name__ == '__main__':
    test_case = [3, 4, 2, 1, 4, 4, 3]
    print(get_counter(test_case))
    print(Counter(test_case))
