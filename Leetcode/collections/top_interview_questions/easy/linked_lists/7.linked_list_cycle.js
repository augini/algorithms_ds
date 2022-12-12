/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */

var hasCycle = function (head) {
  if (!head) return false;

  let slowPointer = head,
    fastPointer = head.next;

  while (1) {
    if (!fastPointer || !fastPointer.next) return false;
    if (slowPointer === fastPointer || slowPointer === fastPointer.next) {
      return true;
    }

    slowPointer = slowPointer.next;
    fastPointer = fastPointer.next.next;
  }
};
