# The isBadVersion API is already defined for you.
# https://leetcode.com/problems/first-bad-version/description/?envType=study-plan&id=algorithm-i


def isBadVersion(version: int) -> bool:
    return True


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n

        while start < end:
            mid = (start + end) // 2

            if isBadVersion(mid):
                end = mid
            elif isBadVersion(mid) == False:
                start = mid + 1

        return start
