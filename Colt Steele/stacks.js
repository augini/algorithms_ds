class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = null;
  }

  push(value) {
    let newNode = new Node(value);
    if (!this.first) {
      this.first = newNode;
      this.last = newNode;
    } else {
      let temp = this.first;
      this.first = newNode;
      this.first.next = temp;
    }

    this.size++;
    return this;
  }

  pop() {
    let temp;
    if (!this.first) {
      return null;
    } else if (this.size === 1) {
      temp = this.first;
      this.first = null;
      this.last = null;
    } else {
      temp = this.first;
      this.first = temp.next;
      temp.next = null;
    }

    this.size--;
    return temp.value;
  }
}
