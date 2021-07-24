// Complete the hasCycle function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

function hasCycle(head) {
  if (!head) {
    return null;
  }

  let slow = head;
  let fast = head;

  while (fast.next.next) {
    fast = fast.next.next;
    slow = slow.next;
    if (fast === slow) {
      return 1;
    }
  }

  return 0;
}
