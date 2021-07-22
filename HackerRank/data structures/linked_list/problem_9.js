/*
 * Complete the 'getNode' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_SINGLY_LINKED_LIST llist
 *  2. INTEGER positionFromTail
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

function getNode(llist, positionFromTail) {
  if (!llist) {
    return null;
  }

  let current = llist;
  let values = [];

  while (current.next) {
    values.push(current.data);
    current = current.next;
  }

  return values[values.length - positionFromTail];
}

// TAKEAWAY || APPROACH
