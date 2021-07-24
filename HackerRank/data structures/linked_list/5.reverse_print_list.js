//LINK : https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem?h_r=next-challenge&h_v=zen

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

function reversePrint(llist) {
  if (!llist) {
    return null;
  }

  let temp = llist;
  let values = [];

  while (temp) {
    values.push(temp.data);
    temp = temp.next;
  }

  values = values.reverse();

  values.forEach((item) => {
    console.log(item);
  });
}
