from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counter = Counter(s)
        most_freq_chars = []

        for char, count in char_counter.items():
            most_freq_chars.append([-count, char])

        heapq.heapify(most_freq_chars)

        previous = None
        result = ""

        while len(most_freq_chars) > 0 or previous:
            if previous and len(most_freq_chars) == 0:
                return ""

            count, char = heapq.heappop(most_freq_chars)
            result = result + char
            count = count + 1

            if previous:
                heapq.heappush(most_freq_chars, previous)
                previous = None

            if count != 0:
                previous = [count, char]

        return result
