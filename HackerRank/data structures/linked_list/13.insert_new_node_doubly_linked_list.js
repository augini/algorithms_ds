/*
 * Complete the 'sortedInsert' function below.
 *
 * The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
 * The function accepts following parameters:
 *  1. INTEGER_DOUBLY_LINKED_LIST llist
 *  2. INTEGER data
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

function sortedInsert(llist, data) {
  if (!llist) return null;

  let current = llist;
  let newNode = new DoublyLinkedListNode(data);

  if (llist.data > data) {
    newNode.next = llist;
    llist.prev = newNode;
    llist = newNode;
  } else {
    while (current.next && current.next.data < data) {
      current = current.next;
    }

    newNode.next = current.next;
    newNode.prev = current;

    current.next = newNode;
    current.next.prev = newNode;
  }

  return llist;
}
