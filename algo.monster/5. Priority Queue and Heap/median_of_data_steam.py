from heapq import heappush, heappop


class MedianOfStream:
    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def balance_heaps(self):
        l = len(self.left_max_heap)
        r = len(self.right_min_heap)

        if l < r:
            val = heappop(self.right_min_heap)
            heappush(self.left_max_heap, -val)

        if l > r + 1:
            val = - heappop(self.left_max_heap)
            heappush(self.right_min_heap, val)

        return None

    def add_number(self, num: float) -> None:
        l = len(self.left_max_heap)
        r = len(self.right_min_heap)

        if r == 0 or num < self.right_min_heap[0]:
            heappush(self.left_max_heap, -num)

        else:
            heappush(self.right_min_heap, num)

        self.balance_heaps()

        return None

    def get_median(self) -> float:
        if len(self.left_max_heap) == len(self.right_min_heap):
            return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2
        return -self.left_max_heap[0]


if __name__ == '__main__':
    median_of_stream = MedianOfStream()

    n = 10
    ip = ["-1", "get", "-2", "get", "-3", "get", "-4", "get", "-5", "get"]

    for i in range(n):
        line = ip[i].strip()
        if line == 'get':
            median = median_of_stream.get_median()
            print(f'{median:.1f}')
        else:
            num = float(line)
            median_of_stream.add_number(num)
