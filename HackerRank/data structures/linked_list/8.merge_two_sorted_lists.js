//LINK : https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem?h_r=next-challenge&h_v=zen
/*
Complete the mergeLists function below.
/*

 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

function mergeLists(head1, head2) {
  if (head1 && head2) {
    let current = head2;

    // traverse the second list and place the data values into the first list in order
    while (current.next) {
      let pointer = head1;

      // traverse the first list to find the most ordered place for item in the second list
      while (pointer.next) {
        let sample = current;

        if (current.data < pointer.next.data) {
          pointer.next = sample;
          sample.next = pointer.next;
        }

        pointer = pointer.next;
      }

      current = current.next;
    }

    return head1;
  }

  return !head1 ? head2 : head1;
}

// TAKEAWAY || APPROACH
