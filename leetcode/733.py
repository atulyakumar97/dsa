from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        num_rows = len(image)
        num_cols = len(image[0])
        start_pixel = image[sr][sc]
        image[sr][sc] = color

        def get_neighbors(coord):
            root_row, root_col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]

            for i in range(len(delta_row)):
                neighbor_row = root_row + delta_row[i]
                neighbor_column = root_col + delta_col[i]

                if 0 <= neighbor_row < num_rows and 0 <= neighbor_column < num_cols:
                    if image[neighbor_row][neighbor_column] == start_pixel:
                        yield neighbor_row, neighbor_column

        def bfs(root):

            queue = deque([root])
            visited = {[root]}

            while len(queue) > 0:
                node = queue.popleft()

                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue

                    r, c = neighbor
                    image[r][c] = color
                    visited.add(neighbor)
                    queue.append(neighbor)

        bfs((sr, sc))
        return image
