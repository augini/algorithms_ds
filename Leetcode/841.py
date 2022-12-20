# https://leetcode.com/problems/keys-and-rooms/description/

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [rooms[0]]
        keys = set([0])

        while stack:
            curr = stack.pop()

            while curr:
                c = curr.pop()

                if c in keys:
                    continue

                keys.add(c)
                stack.append(rooms[c])

        return len(keys) == len(rooms)
