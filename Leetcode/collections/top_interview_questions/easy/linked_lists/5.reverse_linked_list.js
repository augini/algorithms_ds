/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

// imperative approach
var reverseList = function (head) {
  if (!head) {
    return null;
  } else if (!head.next) {
    return head;
  } else if (!head.next.next) {
    let newHead = head.next;
    head.next = null;
    newHead.next = head;
    return newHead;
  }

  let last = head;
  let second = head.next;
  let first = head.next.next;

  last.next = null;

  while (first.next) {
    second.next = last;

    last = second;
    second = first;
    first = first.next;
  }

  first.next = second;
  second.next = last;

  return first;
};

// recursive approach
