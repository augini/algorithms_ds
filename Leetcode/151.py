# https://leetcode.com/problems/reverse-words-in-a-string/description/


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = list(reversed(s))

        stack = []

        for item in s:
            if item != "":
                stack.append(item)

        return " ".join(stack).strip()
