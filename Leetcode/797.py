from typing import List
from copy import deepcopy
from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        l = len(graph)
        start, target = 0, l - 1

        nodes = defaultdict(set)
        for i in range(l):
            nodes[i] = graph[i]

        stack = [(start, [0])]
        results = []
        while stack:
            curr = stack.pop()
            node, path = curr

            if node == target:
                results.append(path)

            if nodes[node]:
                for item in nodes[node]:
                    temp = deepcopy(path)
                    temp.append(item)
                    stack.append((item, temp))

        return results
