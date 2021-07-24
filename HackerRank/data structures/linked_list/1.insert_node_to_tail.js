// Inserting a node to the tail of a list
// LINK: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

// SOLUTION:
/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
function insertNodeAtTail(head, data) {
  const newNode = new SinglyLinkedListNode(data);

  if (!head) {
    head = newNode;
    return head;
  }

  let temp = head;

  while (temp.next) {
    temp = temp.next;
  }

  temp.next = newNode;

  return head;
}

// TAKEAWAY || APPROACH
// First, need to handle the edge case that is if the head is null
// Second, needed to assign a pointer to the head and traverse the list to get to the last item
// Third, needed to use the same built in data structure in js itself
