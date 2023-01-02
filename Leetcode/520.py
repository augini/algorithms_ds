class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        all = True
        notAll = True
        firstIndex = False

        l = len(word)

        for i in range(l):
            if i == 0 and word[i].isupper():
                firstIndex = True
            elif word[i].isupper():
                notAll = False
                firstIndex = False
            elif word[i].islower():
                all = False

        return all or notAll or firstIndex
