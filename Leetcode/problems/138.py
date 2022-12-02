# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        oldToNewCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToNewCopy[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copy = oldToNewCopy[cur]
            copy.next = oldToNewCopy[cur.next]
            copy.random = oldToNewCopy[cur.random]
            cur = cur.next

        return oldToNewCopy[head]
