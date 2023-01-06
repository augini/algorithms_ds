# https://leetcode.com/problems/letter-case-permutation/description/?envType=study-plan&id=algorithm-i

from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        allPerms: List[str] = []

        def dfs(word: str, curr: int):
            if curr == len(word):
                return

            if word[curr].isalpha():
                for i in range(len(allPerms)):
                    current = list(allPerms[i])

                    if current[curr].islower():
                        current[curr] = current[curr].upper()
                    else:
                        current[curr] = current[curr].lower()

                    allPerms.append("".join(current))

            dfs(word, curr + 1)

        s = list(s)
        allPerms.append("".join(s))
        dfs(s, 0)

        return allPerms
