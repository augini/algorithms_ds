# https://leetcode.com/problems/min-stack/description/
import math


class MinStack:
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val: int) -> None:
        self.data.append(val)

        if len(self.min) == 0 or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if self.min[-1] == self.data.pop():
            self.min.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
