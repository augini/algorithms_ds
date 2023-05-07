# https://leetcode.com/problems/k-closest-points-to-origin/
from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # n = len(points)

        # O(n)
        for x, y in points:
            # calculate dist
            dist = x**2 + y**2
            heap.append((dist, x, y))

        # O(log(n))
        heapq.heapify(heap)

        res = []
        # O(k)
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append((x, y))
            k -= 1

        return res


# n -> len(points)
# Time complexity O(n)
# Space O(n)
