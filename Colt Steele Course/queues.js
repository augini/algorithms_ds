class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class Queues {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = null;
  }

  enqueue(value) {
    let newNode = new Node(value);
    if (!this.first) {
      this.first = newNode;
      this.last = newNode;
    } else {
      this.last.next = newNode;
      this.last = newNode;
    }

    this.size++;
    return this;
  }

  dequeue() {
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
