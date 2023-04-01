# https://leetcode.com/problems/power-of-two/description/?envType=study-plan&id=algorithm-i

from collections import Counter


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False

        n = bin(n)
        c = Counter(n)

        return c["1"] == 1
