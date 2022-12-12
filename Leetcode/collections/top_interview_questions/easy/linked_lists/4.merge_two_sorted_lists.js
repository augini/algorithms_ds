/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const mergeTwoLists = (l1, l2) => {
  // if any of the arrays is empty, return another one

  if (!l1 && !l2) {
    return null;
  } else if (!l2 && l1) {
    return l1;
  } else if (!l1 && l2) {
    return l2;
  }

  let min = l1.val <= l2.val ? l1 : l2;
  let max = l1.val > l2.val ? l1 : l2;

  let fastPointer = min.next ? min.next : min,
    slowPointer = min;

  let targetPointer = max;
  if (!max.next) {
    while (fastPointer.next || fastPointer.value < max.value) {
      slowPointer = fastPointer;
      fastPointer = fastPointer.next;
    }

    if (slowPointer.next) {
      max.next = slowPointer.next;
    }
    slowPointer.next = max;
    return min;
  }

  while (targetPointer) {
    // console.log(targetPointer.val);

    if (targetPointer.val <= fastPointer.val) {
      let temp = targetPointer;
      targetPointer = targetPointer.next;

      temp.next = slowPointer.next;
      slowPointer.next = temp;

      slowPointer = slowPointer.next;
    } else if (!fastPointer.next) {
      let temp = targetPointer;
      targetPointer = targetPointer.next;

      temp.next = null;
      fastPointer.next = temp;

      slowPointer = fastPointer;
      fastPointer = fastPointer.next;
    } else {
      slowPointer = slowPointer.next;
      fastPointer = fastPointer.next ? fastPointer.next : fastPointer;
    }
  }

  return min;
};
