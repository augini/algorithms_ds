# https://leetcode.com/problems/sum-of-distances-in-tree/description/
from collections import defaultdict, deque
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * n
        output = [0] * n
        self.root = 0

        def dfs(curr, parent, depth):
            o = 1

            for node in graph[curr]:
                if node != parent:
                    o += dfs(node, curr, depth + 1)
                    self.root += depth + 1
            count[curr] = o
            return o

        dfs(0, None, 0)
        #   print(count, self.root)

        def dfs2(curr, parent, ans_p):
            output[curr] = ans_p
            for child in graph[curr]:
                if child != parent:
                    dfs2(child, curr, ans_p + (n - count[child]) - count[child])

        dfs2(0, -1, self.root)

        return output
