from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        steps = 0

        for value in c.values():
            if value == 1:
                return -1
            else:
                steps += value // 3 + min(1, value % 3)
        return steps
