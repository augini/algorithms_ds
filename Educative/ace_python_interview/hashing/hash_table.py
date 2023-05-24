from typing import Any


# The implementation of hash table from inside code
class Node:
    def __init__(self, key, value, next=None):
        self.key: str = key
        self.value: Any = value
        self.next: None = next


class LinkedList:
    def __init__(self, head=None):
        self.head: Node = head

    def insert(self, key, value):
        new_node = Node(key, value, self.head)
        self.head = new_node

    def search(self, key):
        node = self.head
        while node:
            if node.key == key:
                return node
            node = node.next
        return None

    def delete(self, key):
        if self.head and self.head.key == key:
            self.head = self.head.nxt
            return True
        else:
            node = self.head
            while node and node.nxt and node.nxt.key != key:
                node = node.nxt
            if node:
                node.nxt = node.nxt.nxt
                return True
        return False
