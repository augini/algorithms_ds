//LINK: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

function insertNodeAtPosition(llist, data, position) {
  let newNode = new SinglyLinkedListNode(data);

  let temp = llist.head;
  let counter = 0;

  while (counter <= position || temp) {
    temp = temp.next;
    counter++;
  }

  newNode.next = temp.next;
  temp.next = newNode;

  return llist;
}

// TAKEAWAY || APPROACH

function insertNodeAtPosition(llist, data, position) {
  // If list is empty, insert data at 0
  let newNode = new SinglyLinkedListNode(data);

  if (!llist) {
    llist.head = newNode;
  } else if (position === 0) {
    newNode.next = llist.head;
    llist.head = newNode;
  } else {
    let current = llist;
    let counter = 0;

    while (counter < position - 1 && current) {
      current = current.next;
      counter++;
    }
    let next = current.next;
    current.next = newNode;
    newNode.next = next;
  }

  return llist;
}
