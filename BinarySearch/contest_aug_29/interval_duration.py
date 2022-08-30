# https://binarysearch.com/problems/Interval-Duration

class Solution:
    def solve(self, iv):
        iv.sort()
        uvi = []

        length = len(iv)

        for i in range(length):
            if not uvi or iv[i][0] > uvi[-1][1]:
                uvi.append(iv[i])

            elif iv[i][0] <= uvi[-1][1] and iv[i][1] > uvi[-1][1]:
                uvi[-1][1] = iv[i][1]

        total = 0
        
        for item in uvi:
            total+=item[1] - item[0] + 1
        return total
