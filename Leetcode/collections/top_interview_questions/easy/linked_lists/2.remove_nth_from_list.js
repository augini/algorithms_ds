/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  // Maintain two pointers and update one with a delay of n steps.
  let first = head;
  let second = head;

  // move the first pointer n steps ahead
  for (let i = 0; i < n; i++) {
    if (first.next === null) {
      // if n is equal to the number of steps, delete the head node
      if (i == n - 1) {
        head = head.next;
      }
      return head;
    }
    first = first.next;
  }

  // Loop until we reach to the end.
  // Now we will move both fast and slow pointers
  while (first.next !== null) {
    second = second.next;
    first = first.next;
  }
  // Delink the nth node from last
  if (second.next !== null) {
    second.next = second.next.next;
  }
  return head;
};
