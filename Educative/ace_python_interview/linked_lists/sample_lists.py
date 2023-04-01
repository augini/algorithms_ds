# Linked Lists

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head  # O(1)

    def is_empty(self):
        return self.head is None  # O(1)

    def insert_at_head(self, data):  # O(1)
        node = Node(data)

        node.next = self.head
        self.head = node

        return self.head

    def delete_head(self):  # O(1)
        temp = self.get_head()

        if temp:
            self.head = temp.next
            temp.next = None

        return

    def insert_at_tail(self, data):  # O(n)
        node = Node(data)

        if self.is_empty():
            self.head = node
            return

        temp = self.get_head()
        while temp.next:
            temp = temp.next

        temp.next = node
        return

    def insert_at_index(self, data, index):

        if self.is_empty():
            return False

        temp = self.head
        counter = 1

        while temp.next and counter < index:
            counter += 1
            temp = temp.next

        # index is larger than size
        if counter < index:
            print("Index is larger than size")
            return False

        node = Node(data)

        # set node next
        node.next = temp.next
        temp.next = node

        return

    def print_list(self):
        if self.is_empty():
            print("List is empty")
            return

        temp = self.head
        while temp.next:
            print(temp.data, end=" -> ")
            temp = temp.next

        print(temp.data, end=" -> None \n")
        return True


llist = LinkedList()
llist.print_list()

llist.insert_at_head(15)

llist.insert_at_index(20, 1)
llist.insert_at_index(35, 2)

llist.print_list()

llist.delete_head()

llist.print_list()
