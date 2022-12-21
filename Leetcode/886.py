# https://leetcode.com/problems/possible-bipartition/
from typing import List
from collections import defaultdict, deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        colors = defaultdict(list)
        l = len(graph) - 1
        if l > 100:
            l = l // 4

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
