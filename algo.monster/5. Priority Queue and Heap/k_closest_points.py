from typing import List
import math
import heapq


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    h = []
    ans = []

    for point in points:
        dist = math.sqrt((point[0] ** 2) + (point[1] ** 2))
        heapq.heappush(h, (dist, point))

    for i in range(k):
        ans.append(heapq.heappop(h)[1])

    return ans


if __name__ == '__main__':
    points = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = k_closest_points(points, k)
    for row in res:
        print(' '.join(map(str, row)))
