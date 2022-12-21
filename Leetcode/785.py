# https://leetcode.com/problems/is-graph-bipartite/

from collections import defaultdict, deque
from typing import List
from enum import Enum


class Color(Enum):
    kWhite = 0
    kRed = 1
    kGreen = 2


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        visited = set()
        colors = defaultdict(list)
        l = len(graph) - 1

        for i in range(l):
            q = deque([(graph[i], "red")])

            while q:
                t = q.popleft()
                curr, col = t

                while curr:
                    node = curr.pop()
                    if node not in visited:
                        if col == "red":
                            color = "blue"
                        else:
                            color = "red"

                        q.append((graph[node], color))
                        visited.add(node)
                    colors[col].append(node)

        for node in colors["red"]:
            if node in colors["blue"]:
                return False
        return True

    def _isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [Color.kWhite] * len(graph)

        for i in range(len(graph)):
            # Already colored, do nothing
            if colors[i] != Color.kWhite:
                continue
            # colors[i] == Color.kWhite

            colors[i] = Color.kRed  # Always paint w/ Color.kRed
            # BFS
            q = deque([i])

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if colors[v] == colors[u]:
                        return False
                    if colors[v] == Color.kWhite:
                        colors[v] = (
                            Color.kRed if colors[u] == Color.kGreen else Color.kGreen
                        )
                        q.append(v)

            return True


sample = Solution()
print(sample._isBipartite([[3], [7, 9], [], [0, 5], [], [3], [9], [1], [], [1, 6]]))
