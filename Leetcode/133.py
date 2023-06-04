# https://leetcode.com/problems/clone-graph/
from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        clone = defaultdict(Node)

        # push all the nodes into the hashmap using dfs
        def dfs(item: "Node"):
            if item in clone:
                return clone[item]

            clone[item] = Node(item.val)

            for n in item.neighbors:
                clone[item].neighbors.append(dfs(n))

            return clone[item]

        return dfs(node)
