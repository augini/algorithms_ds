class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert(input) {
    let newNode = new Node(input);

    if (!this.root) {
      return (this.root = newNode);
    }

    let current = this.root;

    while (true) {
      if (input === current.value) return undefined;

      if (input < current.value) {
        if (current.left === null) {
          current.left = newNode;
          return this;
        }
        current = current.left;
      } else if (input > current.value) {
        if (current.right === null) {
          current.right = newNode;
          return this;
        }
        current = current.right;
      }
    }
  }

  contains(input) {
    if (!this.root) {
      return false;
    }

    let current = this.root;

    while (true) {
      if (input === current.value) {
        return true;
      } else if (input > current.value) {
        if (current.right === null) {
          return false;
        }
        current = current.right;
      } else if (input < current.value) {
        if (current.left === null) {
          return false;
        }
        current = current.left;
      }
    }
  }

  find(input) {
    if (!this.root) {
      return false;
    }

    let current = this.root;

    while (true) {
      if (input === current.value) {
        return current;
      } else if (input > current.value) {
        if (current.right === null) {
          return false;
        }
        current = current.right;
      } else if (input < current.value) {
        if (current.left === null) {
          return false;
        }
        current = current.left;
      }
    }
  }
}

const tree = new BinarySearchTree();
// tree.root = new Node(12);
// tree.root.right = new Node(15);

tree.insert(10);
tree.insert(5);
tree.insert(13);
tree.insert(11);
tree.insert(2);
tree.insert(16);

console.log(tree);

console.log(tree.find(10));
