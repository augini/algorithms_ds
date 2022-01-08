//

const create_adjacency_list = (edges) => {
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
  return dictionary;
};

const find_shortest_path = (graph, start, end) => {
  const adjacency_list = create_adjacency_list(graph);

  const stack = [[start, ""]];
  let visited_nodes = [];
  let distances = [];

  while (stack.length > 0) {
    const current = stack.pop();
    let [node, history] = current;

    history = `${history.length ? history + "," : ""}${node}`;

    if (node === end) {
      distances.push(history.split(",").length - 1);
      continue;
    }

    visited_nodes.push(node);

    adjacency_list[node].forEach((_node) => {
      if (!visited_nodes.includes(_node)) {
        stack.push([_node, history]);
      }
    });
  }

  return distances.length ? Math.min(...distances) : -1;
};

const map = [
  ["w", "x"],
  ["x", "y"],
  ["z", "y"],
  ["z", "v"],
  ["w", "v"],
];

console.log(find_shortest_path(map, "y", "x"));
