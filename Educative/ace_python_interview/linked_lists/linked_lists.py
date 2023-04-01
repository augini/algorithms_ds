# Node: data, next

# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # time complexity: O(1)
    def insert_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

        return self.head

    # O(n)
    def delete_at_index(self, index):
        if self.is_empty():
            return False

        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return

        counter = 1
        temp = self.head

        while temp and counter < index:
            temp = temp.next
            counter += 1

        if counter < index:
            print("Size is smaller than the given index")
            return False

        if temp.next and temp.next.next:
            prev = temp.next
            temp.next = temp.next.next
            prev.next = None
        else:
            temp.next = None

        return

    # O(n)
    def insert_tail(self, data):
        if self.is_empty():
            return False

        temp = self.head

        while temp.next:
            temp = temp.next

        node = Node(data)
        temp.next = node
        return

    # O(n)
    def insert_at_index(self, data, index):

        if self.is_empty():
            return False

        temp = self.head
        counter = 1

        while temp.next and counter < index:
            counter += 1
            temp = temp.next

        if counter < index:
            print("Index is larger than list size")
            return False

        # inserts a new node at a given index
        node = Node(data)
        node.next = temp.next
        temp.next = node

        return

    # O(n)
    def print(self):
        if not self.is_empty():
            temp = self.head

            while temp.next:
                print(temp.data, end=" -> ")
                temp = temp.next
            print(temp.data, end=" -> None")
        else:
            print("List is empty")


llist = LinkedList()
llist.insert_head(5)
llist.print()
print("\n")
llist.insert_at_index(10, 1)
llist.print()
llist.insert_tail(30)
print("\n")
llist.print()
llist.insert_tail(35)
print("\n")
llist.print()
llist.delete_at_index(0)
print("\n")
llist.print()
