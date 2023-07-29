# https://leetcode.com/problems/daily-temperatures/description/
from typing import List


class Solution:
    def _dailyTemperatures(self, temperatures: List[int]) -> List[int]:
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

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)

        stack = []
        result = [0 for i in range(l)]

        for i, v in enumerate(temperatures):
            while stack:
                if temperatures[i] > temperatures[stack[-1]]:
                    prev_index = stack.pop()
                    result[prev_index] = i - prev_index
                else:
                    break
            stack.append(i)
        return result


sample = Solution()
print(sample.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# Time Complexity: O(n)
# Space Complexity: O(n)
