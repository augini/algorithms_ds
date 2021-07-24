//LINK : https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

function deleteNode(head, position) {
  if (!head) {
    return null;
  }

  let temp = head;
  let counter = 0;

  while (temp) {
    if (position === 0) {
      head = temp.next;
      temp = null;
      break;
    } else if (counter === position - 1) {
      temp.next = temp.next.next;
    }
    temp = temp.next;
    counter = counter + 1;
  }

  return head;
}
