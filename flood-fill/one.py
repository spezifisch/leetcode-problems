from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, new_color: int
    ) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        old_color = image[sr][sc]
        if old_color == new_color:
            return image

        queue = deque()
        queue.append((sr, sc))

        while len(queue):
            r, c = queue.popleft()
            if image[r][c] == new_color:
                continue

            image[r][c] = new_color

            for offset_r, offset_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor_r = r + offset_r
                neighbor_c = c + offset_c
                if neighbor_r < 0 or neighbor_c < 0:
                    continue
                if neighbor_r >= rows or neighbor_c >= cols:
                    continue

                if image[neighbor_r][neighbor_c] == old_color:
                    queue.append((neighbor_r, neighbor_c))

        return image


# Runtime: 80 ms, faster than 21.96% of Python3 online submissions for Flood Fill.
# Memory Usage: 13.1 MB, less than 6.33% of Python3 online submissions for Flood Fill.
