/*
    Find merge point of two linked lists
    Note that the head may be 'null' for the empty list.
    Node is defined as
    var Node = function(data) {
        this.data = data;
        this.next = null;
    }
*/

// This is a "method-only" submission.
// You only need to complete this method.

// Approach taken from
// https://stackoverflow.com/questions/1594061/check-if-two-linked-lists-merge-if-so-where/14956113#14956113

function findMergeNode(headA, headB) {
  if (!headA | !headB) {
    return null;
  }

  let currentA = headA;
  let currentB = headB;

  while (currentA !== currentB) {
    // first pointer
    if (currentA.next) {
      currentA = currentA.next;
    } else {
      currentA = headB;
    }

    // second  pointer
    if (currentB.next) {
      currentB = currentB.next;
    } else {
      currentB = headA;
    }
  }

  return currentA.data;
}

function findMergeNode(headA, headB) {
  if (!headA | !headB) {
    return null;
  }

  let currentA = headA;
  let currentB = headB;

  while (currentA.next) {
    let temp = currentA.next;
    currentA.next = null;
    currentA = temp;
  }

  while (currentB.next) {
    currentB = currentB.next;
  }

  return currentB.data;
}
