# https://binarysearch.com/room/Kadane's-Room-XCwwzSTaWX

class Solution:
    def solve(self, s):
        stack = []

        for item in s:
            if item == "(":
                stack.append(item)
            else: 
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()

        if stack:
            return False

        return True
            