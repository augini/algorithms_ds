/*
 * Complete the 'removeDuplicates' function below.
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

function removeDuplicates(llist) {
  if (!llist) {
    return null;
  }

  let current = llist;

  while (current.next) {
    if (current.data === current.next.data) {
      current.next = current.next.next;
      continue;
    }

    current = current.next;
  }

  return llist;
}
