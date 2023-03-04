from heapq import heappush, heappop
from collections import Counter


def reorganize_string(s: str) -> str:
    hm = Counter(s)
    heap = []
    n = len(s)

    for char, freq in hm.items():
        heappush(heap, (-freq, char))

    # -heap[0][0] is max_freq
    if - heap[0][0] > (n + 1) // 2:
        return ""

    res = [''] * n
    ptr = 0
    while heap:
        freq, char = heappop(heap)

        for _ in range(-freq):
            res[ptr] = char
            ptr += 2

            if ptr >= n:
                ptr = 1

    return ''.join(res)


if __name__ == '__main__':
    s = "lllllooooooooolllll"
    res = reorganize_string(s)
    if not res:
        print("Impossible")
        exit()
    input_counter, output_counter = Counter(s), Counter(res)
    if input_counter != output_counter:
        print("Not rearrangement")
        exit()
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            print(f"Same character at index {i} and {i + 1}")
            exit()
    print("Valid")
