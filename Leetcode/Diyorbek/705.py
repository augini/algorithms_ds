# https://leetcode.com/problems/design-hashset/description/
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self):
        self.max_size = 10**4
        self.array = [None for _ in range(self.max_size)]

    def _hash(self, number):
        return number % self.max_size

    def add(self, key: int) -> None:
        position = self._hash(key)
        if not self.array[position]:
            self.array[position] = Node(key)
        else:
            cur = self.array[position]
            if cur.val == key:
                return
            while cur.next:
                if cur.val == key:
                    return
                cur = cur.next
            cur.next = Node(key)

    def remove(self, key: int) -> None:
        position = self._hash(key)
        node = self.array[position]
        prev = None
        if node and node.val == key:
            self.array[position] = node.next
            return
        prev = None
        while node:
            if node.val == key:
                prev.next = node.next
                break
            prev = node
            node = node.next

    def contains(self, key: int) -> bool:
        position = self._hash(key)
        node = self.array[position]
        while node:
            if node.val == key:
                return True
            node = node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
