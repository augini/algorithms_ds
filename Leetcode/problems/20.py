# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {")": "(", "}": "{", "]": "["}
        opening = ["(", "{", "["]

        if len(s) == 1 or s[0] not in opening:
            return False

        for item in s:
            if item in opening:
                stack.append(item)
            else:
                if stack and pairs[item] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
