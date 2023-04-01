# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

from collections import defaultdict, List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        nodes = defaultdict(list)

        for u, v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        visited = set()
        paths = defaultdict(int)

        def dfs(node, parent):
            visited.add(node)
            totalTime, childTime = 0, 0

            for item in nodes[node]:
                if item != parent and item not in visited:
                    childTime = dfs(item, node)

                    if hasApple[item] or childTime > 0:
                        totalTime += childTime + 2
            return totalTime

        return dfs(0, -1)
