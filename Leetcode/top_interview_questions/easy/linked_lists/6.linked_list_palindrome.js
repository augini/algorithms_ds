/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  const isPalindromeRecursive = (recursiveHead) => {
    if (recursiveHead === null) {
      return true;
    }

    const next = isPalindromeRecursive(recursiveHead.next);
    const valid = recursiveHead.val === head.val;

    head = head.next;
    return next && valid;
  };

  return isPalindromeRecursive(head);
};
