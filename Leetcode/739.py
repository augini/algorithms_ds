# https://leetcode.com/problems/daily-temperatures/description/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)

        stack = [0 for i in range(length)]
        result = [0 for i in range(length)]

        for i in range(length):
            if len(stack) > 0:
                while True and len(stack):
                    if temperatures[i] > temperatures[stack[-1]]:
                        item = stack.pop()
                        result[item] = i - item
                    else:
                        break
            stack.append(i)
        return result


# Time Complexity: O(n)
# Space Complexity: O(n)
