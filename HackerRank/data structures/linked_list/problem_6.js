//LINK : https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

/*
 * Complete the 'reverse' function below.
 *
 * The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
 * The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
 */

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

function reverse(llist) {
  // Write your code here

  let prev = null;
  let next = null;

  let current = llist;
  while (current.next) {
    next = current.next;
    current.next = prev;

    prev = current;
    current = next;
  }

  current.next = prev;
  llist = current;

  return llist;
}

// TAKEAWAY || APPROACH
