from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not len(prerequisites):
            return True

        edges = defaultdict(list)
        for a, b in prerequisites:
            edges[a].append(b)

        visited = set()

        def dfs(edge):
            if edge in visited:
                return False
            if edges[edge] == []:
                return True

            visited.add(edge)
            for crs in edges[edge]:
                if not dfs(crs):
                    return False

            visited.remove(edge)
            edges[edge] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
