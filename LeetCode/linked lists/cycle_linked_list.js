console.log("working on cycled linked list");

var detectCycle = function (head) {
  if (!head) {
    return null;
  }

  // declare slow and fast pointers
  const slow = head;
  const fast = head;

  while (slow !== fast) {
    // if fast reaches null, that means the end of list without cycle
    if (fast === null || fast.next === null) {
      return false;
    }

    slow = slow.next;
    fast = fast.next.next;
  }

  // if they are equal, we saw a cycle
  return true;
};
