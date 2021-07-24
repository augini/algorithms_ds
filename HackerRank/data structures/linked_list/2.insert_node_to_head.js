// Inserting a node to the head of a list
// LINK: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem?h_r=next-challenge&h_v=zen

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
function insertNodeAtHead(head, data) {
  let newNode = new SinglyLinkedListNode(data);

  if (!head) {
    head = newNode;
    return head;
  }

  newNode.next = head;
  head = newNode;

  return head;
}

// TAKEAWAY || APPROACH
