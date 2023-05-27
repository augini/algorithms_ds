# https://leetcode.com/problems/time-based-key-value-store/
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.list = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.list[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # return false if key doesn't exist or timetamp is smaller than lowest timestamp for that key
        if not self.list[key] or (
            self.list[key][0] and timestamp < self.list[key][0][0]
        ):
            return ""
        else:
            # do a binary search between timestamps
            start, end = 0, len(self.list[key])

            while start < end:
                mid = (start + end) // 2
                curr = self.list[key][mid]

                if curr[0] < timestamp:
                    start = mid + 1
                elif curr[0] > timestamp:
                    end = mid
                elif curr[0] == timestamp:
                    return curr[1]

            stopped_at = self.list[key][mid]
            return (
                self.list[key][mid - 1][1]
                if stopped_at[0] > timestamp
                else stopped_at[1]
            )


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap().
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
