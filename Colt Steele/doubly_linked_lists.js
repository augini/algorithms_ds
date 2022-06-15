class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(data) {
    let newNode = new Node(data);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      let temp = this.tail;
      this.tail.next = newNode;
      newNode.prev = temp;
      this.tail = newNode;
    }

    this.length++;
    return this;
  }

  pop() {
    // 1. Check if the list is empty, return null if it is
    // 2. Set the next element on the node before the tail to be null
    // 3. Handle the special case where the list length is 1
    // 4. Set the tail of the list to be the node one before the tail

    if (!this.head) {
      return null;
    }
    let oldTail = this.tail;

    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    }

    let newTail = this.tail.prev;
    newTail.next = null;
    oldTail.prev == null;
    this.tail = newTail;

    this.length--;
    return oldTail;
  }

  /**
   * Returns the head node and removes it from the list
   * 1. Check if the list is empty, return null if it is
   * 2. If the length is one, set head and tail to null
   * 3. Store the head in a temp node and set the head to be the next of the head
   * 4. Set the next of temp to null and the prev of the current head to null
   * 5. Decrement the length and return the removed node
   */
  shift() {
    if (!this.head) return null;

    let oldHead = this.head;

    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = oldHead.next;
      oldHead.next = null;
      this.head.prev = null;
    }

    this.length--;
    return oldHead;
  }

  /**
   * Add a new node to the beginning of the list
   * 1. Check if the list is empty, set the head and tail to a new node if it is
   * 2. Set the next of new node to be head
   * 3. Set the prev of head to be new node
   * 4. Set the head to be new node
   * 5. Increment the length and return the list
   */
  unshift(data) {
    let newNode = new Node(data);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head.prev = newNode;
      this.head = newNode;
    }

    this.length++;
    return this;
  }

  /**
   * Get the node at a specific position in a list
   * 1. If the index is equeal to 0 or greater than the length, return null
   * 2. Find if the index is closer to head or tail
   * 3. If it is closer to head, use next to traverse the list and get item
   * 4. If it is closer to tail, use prev of tail to traverse the list and get item
   * 5. Return the node at the specific index
   */
  get(index) {
    if (index < 0 || index > this.length) {
      return null;
    }

    let current;

    if (index <= this.length / 2) {
      let counter = 0;
      current = this.head;

      while (counter != index) {
        current = current.next;
        counter++;
      }
    }

    if (index > this.length / 2) {
      let counter = this.length - 1;
      current = this.tail;

      while (counter != index) {
        current = current.prev;
        counter--;
      }
    }

    return current;
  }

  /**
   * Set the node at a specific position in a list with a given value
   * 1. Get a certain node with get method
   * 2. If get method returns valid node, update the value of that node
   * 3. return true if updated, otherwise return false
   */
  set(index, data) {
    let updateNode = this.get(index);
    if (updateNode) {
      updateNode.value = data;
      return true;
    }
    return false;
  }

  /**
   * Insert a new node at a given position with a given value
   * 1. If the index is less than 0 or greater  than length, return false
   * 2. If the index is 0, unshift
   * 3. If the index is same as the length, push
   * 4. Use the get method to get the node at index-1
   * 5. Set the next and prev properties on correct nodes to link everything together
   */
  insert(index, data) {
    if (index < 0 || index > this.length) {
      return false;
    } else if (index === 0) {
      this.unshift(data);
    } else if (index === this.length) {
      this.push(data);
    } else {
      let newNode = new Node(data);

      let prevNode = this.get(index - 1);

      newNode.next = prevNode.next;
      newNode.prev = prevNode;

      prevNode.next.prev = newNode;
      prevNode.next = newNode;

      this.length++;
    }

    return true;
  }

  /**
   * Insert a new node at a given position with a given value
   * 1. If the index is less than 0 or greater  than length, return false
   * 2. If the index is 0, shift
   * 3. If the index is same as the length-1, pop
   * 4. Use the get method to get the node at index
   * 5. Set the next and prev properties on correct nodes to link everything together
   * 6. Return the removed node
   */
  remove(index) {
    if (index < 0 || index > this.length) {
      return false;
    } else if (index === 0) {
      return this.shift();
    } else if (index === this.length) {
      return this.pop();
    }

    let foundNode = this.get(index);

    foundNode.prev.next = foundNode.next;
    foundNode.next.prev = foundNode.prev;

    foundNode.next = null;
    foundNode.prev = null;

    this.length--;

    return foundNode;
  }
}
