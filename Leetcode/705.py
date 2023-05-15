# https://github.com/augini/_algorithms_ds/pull/2/commits/700cb08bfee1f01d0864ade546fde6f13d6a059a
class SetNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyHashSet:
    def __init__(self):
        self.upper_limit = 10**4
        self.items = [None for _ in range(self.upper_limit)]

    def _hash(self, num: int):
        return num % self.upper_limit

    def add(self, key: int) -> None:
        # generate a hash of the key
        index = self._hash(key)
        # place an item in that index
        if self.items[index]:
            # if a list already exist, update head
            curr = self.items[index]
            if curr.val == key:
                return
            itemToInsert = SetNode(key)
            itemToInsert.next = curr
            self.items[index] = itemToInsert
        else:
            # if not place the node there
            self.items[index] = SetNode(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.items[index]

        if not curr:
            return

        if curr.val == key:
            self.items[index] = curr.next
            curr.next = None

        prev = None

        while curr and curr.val != key:
            prev = curr
            curr = curr.next
        if prev:
            nextItem = curr.next if curr.next else None
            prev.next = nextItem

        return None

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        curr = self.items[index]
        while curr:
            if curr.val == key:
                return True
            curr = curr.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
