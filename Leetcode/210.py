# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)

        for a, b in prerequisites:
            edges[a].append(b)

        visited = set()
        order = set()

        def dfs(edge):
            if edge in visited:
                return []
            if edges[edge] == []:
                return True

            visited.add(edge)
            for crs in edges[edge]:
                if not dfs(crs):
                    return []

            visited.remove(edge)
            edges[edge] = []
            return True

        for i in range(numCourses):
            order.add(i)
            if not dfs(i):
                return []

        return list(order)
