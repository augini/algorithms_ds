# https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/865980330/?envType=study-plan&id=algorithm-i


class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseWord(word):
            left, right = 0, len(word) - 1

            while left < right:
                temp = word[left]
                word[left] = word[right]
                word[right] = temp
                left += 1
                right -= 1
            return word

        words = s.split(" ")

        for i in range(len(words)):
            curr = [*words[i]]
            res = reverseWord(curr)
            words[i] = "".join(res)

        return " ".join(words)
