from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        # indexes = []
        # gas_sum, cost_sum = sum(gas), sum(cost)

        # for i in range(length):
        #     if gas[i] - cost[i] >= 0:
        #         indexes.append(i)

        ##### approach 1 #####

        # for i in indexes:
        #     diff = gas[i] - cost[i]
        #     if (gas_sum - gas[i]) - (cost_sum - cost[i]) + diff >= 0:
        #         return i

        ##### approach 2 ######

        # for i in indexes:
        #     current = gas[i] - cost[i]
        #     j = i

        #     while True:
        #         if current < 0:
        #             break

        #         if j == i-1:
        #             return i

        #         if j < length - 1:
        #             j +=1
        #         elif j == length - 1:
        #             j = 0
        #         current += gas[j] - cost[j]

        if sum(cost) > sum(gas):
            return -1

        # approach 3
        total = 0
        res = 0

        for i in range(length):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res
