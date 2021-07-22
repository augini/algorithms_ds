//LINK : https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
/*
Complete the CompareLists function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
function CompareLists(llist1, llist2) {
  let first = llist1;
  let firstList = [];

  let second = llist2;
  let secondList = [];

  while (first.next) {
    firstList.push(first.data);
    first = first.next;
  }

  while (second.next) {
    secondList.push(second.data);
    second = second.next;
  }

  if (firstList.length === secondList.length) {
    for (let i = 0; i < firstList.length; i++) {
      if (firstList[i] !== secondList[i]) {
        return 0;
      }
    }

    return 1;
  }

  return 0;
}

// TAKEAWAY || APPROACH
// 1. To compare linked list values, it is okay to pull list values to array and compare those arrays
// 2. Next more optimized solution could be recursion solution as below

function CompareLists(llist1, llist2) {
  // check if the lists are NULL
  if (!llist1 || !llist2) {
    //if both null, the lists are the same length
    return llist1 === llist2 ? 1 : 0;
  }

  // if the data is the same, compare the next node
  return llist1.data === llist2.data
    ? CompareLists(llist1.next, llist2.next)
    : 0;
}
