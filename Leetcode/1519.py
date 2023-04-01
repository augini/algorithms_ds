# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description/
from collections import defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        nodes = defaultdict(list)

        for u, v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        visited = set()
        result = [1] * n

        def dfs(curr, parent):
            count = 1

            visited.add(curr)

            for item in nodes[curr]:
                if item not in visited and item != curr:
                    dfs(item, curr)

            # print(curr, labels[curr], parent, labels[parent], result[curr])

            if labels[curr] == labels[parent] and (parent != -1):
                result[parent] += result[curr]

        dfs(0, -1)

        return result
