/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function (node) {
  const nextNode = node.next;

  // copy the next node value to current node
  node.val = nextNode.val;

  // set the next node to be next next node
  node.next = nextNode.next;

  // unlink the nextNode from the list
  nextNode.next = null;
};
