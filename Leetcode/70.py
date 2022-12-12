# https://leetcode.com/problems/climbing-stairs/


class Solution:
    #  dynamic programming approach
    def _climbStairs(self, n: int) -> int:
        combinations = [1, 1]  # one way to climb zero starirs, one stair

        for x in range(2, n + 1):
            steps = combinations[x - 1] + combinations[x - 2]
            combinations.append(steps)

        return combinations[n]

    def climbStairs(self, n: int) -> int:
        steps = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]
