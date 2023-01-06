from typing import List

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = list(sorted(points, key=lambda item: item[1]))
        length = len(points)

        balloons = 0

        if length == 1:
            return 1

        prevIndex = 0
        for i in range(length):
            if i == 0 or points[i][0] > points[prevIndex][1]:
                balloons += 1
                prevIndex = i

        return balloons
