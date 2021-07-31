/*
 * Complete the 'reverse' function below.
 *
 * The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
 * The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
 */

/*
 * For your reference:
 *
 * DoublyLinkedListNode {
 *     int data;
 *     DoublyLinkedListNode next;
 *     DoublyLinkedListNode prev;
 * }
 *
 */

function reverse(llist) {
  let prev = null;
  let next = null;

  let current = llist;

  while (current.next) {
    next = current.next;
    current.next = prev;
    current.prev = next;

    prev = current;
    current = next;
  }

  current.next = prev;
  llist = current;

  return llist;
}
