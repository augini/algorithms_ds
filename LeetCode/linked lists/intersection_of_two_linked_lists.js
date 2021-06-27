/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function (headA, headB) {
  let visited = [];

  while (headA !== null) {
    visited.push(headA);
    headA = headA.next;
  }

  while (headB !== null) {
    if (visited.includes(headB)) {
      return headB;
    }
    headB = headB.next;
  }

  return null;
};
