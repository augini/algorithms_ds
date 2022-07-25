from collections import Counter, deque

class Solution:
    def solve(self, s, k):
        _count = Counter(s)
        
        changes = 0

        if len(_count.keys()) > k:
            items = deque(sorted(_count.values()))
            while len(items) > k:
                changes+=items.popleft()
            return changes
        return 0