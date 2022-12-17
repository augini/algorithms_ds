# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from collections import deque
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = deque([])
        result = 0
        for item in tokens:
            if item in ["+", "-", "*", "/"]:
                second = s.pop()
                first = s.pop()

                first = int(first)
                second = int(second)

                if item == "+":
                    temp = first + second
                elif item == "-":
                    temp = first - second
                elif item == "/":
                    temp = first / second
                else:
                    temp = first * second
                # print(first, second, temp)
                s.append(temp)

            else:
                s.append(item)

        result = s.pop()
        return int(result)


Sample = Solution()
# print(Sample.evalRPN(["2", "1", "+", "3", "*"]))
print(Sample.evalRPN(["4", "13", "5", "/", "+"]))
# print(
#     Sample.evalRPN(
#         ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
#     )
# )
