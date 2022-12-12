// linked list node simply needs to store
// piece of data -> value
// reference to the next node -> next

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(val) {
    const node = new Node(val);

    if (!this.head) {
      this.head = node;
      this.tail = this.head;
    } else {
      this.tail.next = node;
      this.tail = node;
    }

    this.length++;

    return this;
  }

  pop() {
    if (!this.head) {
      return null;
    }

    let current = this.head;

    if (!current.next) {
      this.head = null;
      this.tail = null;
      this.length--;
      return current;
    }

    while (current.next.next) {
      current = current.next;
    }
    let deleteNode = current.next;

    current.next = null;
    this.tail = current;
    this.length--;

    return deleteNode;
  }

  // version by Colt Steele
  _pop() {
    if (!this.head) return undefined;

    let current = this.head;
    let newTail = current;

    while (!current.next) {
      newTail = current;
      current = current.next;
    }

    this.tail = newTail;
    this.tail.next = null;
    this.length--;
    return current;
  }

  shift() {
    if (!this.head) {
      return null;
    }

    let deleteNode = this.head;
    this.head = this.head.next;
    this.length--;
    return deleteNode;
  }

  unshift(val) {
    let newNode = new Node(val);

    if (!this.head) {
      this.head = newNode;
      this.head = this.tail;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }

    this.length++;
    return this;
  }

  get(index) {
    if (index < 0 || index > this.length) {
      return null;
    }

    let current = this.head;
    let counter = 1;

    while (counter < index) {
      current = current.next;
      counter++;
    }

    return current;
  }

  set(index, value) {
    if (index < 0 || index > this.length) {
      return null;
    }

    let current = this.head;
    let counter = 1;

    while (counter < index) {
      current = current.next;
      counter++;
    }
    current.val = value;

    return this;
  }

  // Colt Steele implementation
  _set(index, value) {
    let foundNode = this.get(index);
    if (foundNode) {
      foundNode.val = value;
      return true;
    }

    return false;
  }

  // Colt Steele implementation
  _set(index, value) {
    let foundNode = this.get(index);
    if (foundNode) {
      foundNode.val = value;
      return true;
    }

    return false;
  }

  insert(index, val) {
    if (index < 0 || index > this.length) {
      return false;
    } else if (index === this.length) {
      this.push(val);
    } else if (index === 0) {
      this.unshift(val);
    } else {
      let newNode = new Node(val);

      let prev = this.get(index - 1);

      newNode.next = prev.next;
      prev.next = newNode;

      this.length++;
    }
    return true;
  }

  remove(index) {
    if (index < 0 || index > this.length) {
      return null;
    }

    if (index === this.length - 1) {
      return this.pop();
    } else if (index === 0) {
      return this.shift();
    } else {
      let prev = this.get(index - 1);
      let temp = prev.next;

      prev.next = temp.next;
      this.length--;

      return temp;
    }
  }

  print() {
    let arr = [];
    let current = this.head;

    while (current) {
      arr.push(current.value);
      current = current.next;
    }

    console.log(arr);
  }

  reverse() {
    this.tail = this.head;

    let next;
    let prev;

    let current = this.head;

    while (current) {
      next = current.next;
      current.next = prev;
      prev = current;

      current = current.next;
    }
  }

  //   Colt Steele version
  _reverse() {
    let current = this.head;

    // swap head and tail
    this.head = this.tail;
    this.tail = current;

    let next = null;
    let prev = null;

    for (let counter = 0; counter < this.length; counter++) {
      next = current.next;
      current.next = prev;

      prev = current;
      current = next;
    }
  }
}

function getNode(llist, positionFromTail) {
  if (!llist) {
    return null;
  }

  let current = llist;
  let values = [];

  while (current) {
    console.log(current);
    values.push(current.value);
    current = current.next;
  }

  console.log(values);

  return values[values.length - positionFromTail];
}

function removeDuplicates(llist) {
  if (!llist) {
    return null;
  }

  let current = llist;

  while (current.next) {
    if (current.value === current.next.value) {
      current.next = current.next.next;
      continue;
    }

    current = current.next;
  }

  return llist;
}

// console.log(removeDuplicates(list.head));

const mergeTwoLists = (l1, l2) => {
  // if any of the arrays is empty, return another one

  if (!l1 && !l2) {
    return null;
  } else if (!l2 && l1) {
    return l1;
  } else if (!l1 && l2) {
    return l2;
  }

  let min = l1.value <= l2.value ? l1 : l2;
  let max = l1.value > l2.value ? l1 : l2;

  let fastPointer = min.next ? min.next : min,
    slowPointer = min;

  let targetPointer = max;

  if (!max.next) {
    while (fastPointer.next && fastPointer.value < max.value) {
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
    // console.log(targetPointer.value);

    if (targetPointer.value <= fastPointer.value) {
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

const list = new SinglyLinkedList();

list.push(-10);
list.push(-10);
list.push(-9);
list.push(-4);
list.push(1);
list.push(6);
list.push(6);

const list_2 = new SinglyLinkedList();
list_2.push(-7);
// list_2.push(7);
// list_2.push(4);

console.log(mergeTwoLists(list.head, list_2.head));
