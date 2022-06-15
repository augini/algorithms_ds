class LinkedListNode {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }

  toString() {
    return callback ? callback(this.value) : `${this.value}`;
  }
}

class LinkedList {
  constructor() {
    /** @var LinkedListNode */
    this.head = null;

    /** @var LinkedListNode */
    this.tail = null;
  }

  prepend(value) {
    // Make a new node to the head
    const newNode = new LinkedListNode(value, this.head);
    this.head = newNode;

    // If there is no tail, let's make new node a tail
    if (!this.tail) {
      this.tail = newNode;
    }

    return this;
  }

  append(value) {
    //Make a new node
    const newNode = new LinkedListNode(value);

    // If there is no head, make this node head
    if (!this.head) {
      this.tail = newNode;
      this.head = newNode;
      return this;
    }

    // Set the next property of our last node to be new node
    this.tail.next = newNode;
    this.tail = newNode;

    return this;
  }

  delete(value) {
    // check if the linked is null
    if (!this.head) {
      return null;
    }

    let deleteNode = null;

    // check if the head is the item to delete
    if (this.head && this.head.value === value) {
      deleteNode = this.head;
      this.head = this.head.next;
    }

    // traverse our list
    let currentNode = this.head;

    if (currentNode !== null) {
      while (currentNode.next) {
        if (currentNode.next.value === value) {
          deleteNode = currentNode.next;
          currentNode.next = currentNode.next.next;
        } else {
          currentNode = currentNode.next;
        }
      }
    }

    // Check if tail must be deleted.
    if (this.tail.value === value) {
      this.tail = currentNode;
    }

    return deleteNode;
  }

  /**
   * @param {Object} findParams
   * @param {*} findParams.value
   * @param {function} [findParams.callback]
   * @return {LinkedListNode}
   */
  find({ value = undefined, callback = undefined }) {
    // there is no head
    if (!this.head) {
      return null;
    }

    // traverse the list
    const currentNode = this.head;

    while (currentNode) {
      // if callback is specified then try to find node by callback
      if (callback && callback(currentNode.value)) {
        return currentNode;
      }

      // if value is specified then try to compare by value
      if (value !== undefined && currentNode.value === value) {
        return currentNode;
      }

      currentNode = currentNode.next;
    }

    // no matching node found
    return null;
  }

  /**
   * @return {LinkedListNode}
   */
  deleteTail() {
    const deletedTail = this.tail;

    // there is only one item in our list
    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;

      return deletedTail;
    }

    // If there are many nodes in linked list...
    // traverse our list
    let currentNode = this.head;

    if (currentNode !== null) {
      while (currentNode.next) {
        if (!currentNode.next.next) {
          currentNode.next = null;
        } else {
          currentNode = currentNode.next;
        }
      }
    }

    this.tail = currentNode;

    return deleteNode;
  }

  /**
   * @return {LinkedListNode}
   */

  deleteHead() {
    // there is no head
    if (!this.head) {
      return null;
    }

    const deleteHead = this.head;

    if (this.head.next) {
      // there are multiple nodes
      this.head = this.head.next;
    } else {
      // there is only one node
      this.head = null;
      this.tail = null;
    }

    return deleteHead;
  }

  /**
   * @param {*[]} values - Array of values that need to be converted to linked list.
   * @return {LinkedList}
   */
  fromArray(values) {
    values.forEach((value) => this.append(value));

    return this;
  }

  /**
   * @return {LinkedListNode[]}
   */
  toArray() {
    const nodes = [];

    let currentNode = this.head;
    while (currentNode) {
      nodes.push(currentNode);
      currentNode = currentNode.next;
    }

    return nodes;
  }

  /**
   * @param {function} [callback]
   * @return {string}
   */
  toString(callback) {
    return this.toArray()
      .map((node) => node.toString(callback))
      .toString();
  }
}
