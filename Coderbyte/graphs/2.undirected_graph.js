// undirected graph traversal

// do a depth first search with stacks
// leave a flag on the visited node
const undirected_graph = (edges, src, dst) => {
  // convert the array to object/dictionary
  let dictionary = {};

  for (let i = 0; i < edges.length; i++) {
    const [x, y] = edges[i];
    dictionary[x] = new Set();
    dictionary[y] = new Set();
  }

  for (let i = 0; i < edges.length; i++) {
    dictionary[edges[i][0]].add(edges[i][1]);
    dictionary[edges[i][1]].add(edges[i][0]);
  }

  // console.log(dictionary);

  let stack = [src];
  let visited = {};
  let path_exists = false;

  while (stack.length > 0) {
    const current_node = stack.pop();
    visited[current_node] = true;

    if (current_node === dst) {
      path_exists = true;
      break;
    }

    Array.from(dictionary[current_node]).forEach((node) => {
      if (!visited[node]) {
        stack.push(node);
      }
    });
  }

  return path_exists;
};

const edges = [
  ["i", "j"],
  ["k", "i"],
  ["m", "k"],
  ["k", "l"],
  ["o", "n"],
];

console.log(undirected_graph(edges, "o", "n"));
