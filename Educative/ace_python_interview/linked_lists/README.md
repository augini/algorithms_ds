# Linked Lists

## Linked Lists vs Lists

The main difference between lists and linked lists is in the way elements are inserted and deleted. As for linked lists, insertion and deletion at the head happen in a `constant amount` of time, whereas at tail, it takes `O(n)` time. In the case of lists, it takes O(n) time to insert or delete a value.

This is because of the different memory layouts of both the data structures. Lists are arranged contiguously in the memory, while nodes of a linked list may be dispersed in the memory. This memory layout also affects access operation; contiguous layout of lists allows us to index the list; thus, access operation in the list is O(1), whereas, for a linked list, we need to perform a traversal thus, it becomes O(n).

| Operation        | Linked List | List            |
| ---------------- | ----------- | --------------- |
| Access           | O(n)        | O(1)            |
| Insert (at head) | O(1)        | O(n)            |
| Delete (at head) | O(1)        | O(n)            |
| Insert (at tail) | O(n)        | O(n) / O(1)\*   |
| Delete (at tail) | O(n)        | O(n) / O(1)\*\* |
| Search           | O(n)        | O(n)            |

> Note:\* Insertion at tail for arrays like data structures is in O(n), but in python, the `append` method for lists is able to do it in O(1).
> Note:\*\* Deletion at tail for arrays like data structures is in O(n), but in python, the pop method for lists is able to do it in O(1).

## Basic Linked List Operations

Basis linked list operations are:

| Operation | Time Complexity |
| --------- | --------------- |
| get_head  | O(1)            |
| is_empty  | O(1)            |

## Singly Linked List Insertion

- Insertion at head
- Inserstion at tail
- Insertion at kth index

## Problem References

[Find the middle node of the linked list](https://leetcode.com/problems/middle-of-the-linked-list/description/)
[Remove the duplicates from a sorted linked list](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
