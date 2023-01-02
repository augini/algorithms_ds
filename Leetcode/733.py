from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        row, column = len(image) - 1, len(image[0]) - 1
        stack = [(sr, sc)]
        st_color = image[sr][sc]
        visited = set()

        while stack:
            y, x = stack.pop()
            image[y][x] = color

            for m, n in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                temp_y = y + m
                temp_x = x + n

                if temp_y < 0 or temp_x < 0 or temp_y > row or temp_x > column:
                    continue

                if (
                    image[temp_y][temp_x] == st_color
                    and (temp_y, temp_x) not in visited
                ):
                    stack.append((temp_y, temp_x))
                    visited.add((temp_y, temp_x))

        return image
