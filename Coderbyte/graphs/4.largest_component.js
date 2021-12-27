// 1. Put every node into a set
// 2. Loop through the set and do a depth first search
// 3. Push every node into visited dictionary to keep track of every node you have visited
// 4. Once the stack is empty, increment the count by one and proceed with the next node in the set
// 5. If that node is not in the visited dictionary, start traversing it, otherwise skip it

const connected_component_count = (graph) => {
  let connection_count = 0;

  let nodes = Object.keys(graph);
  let visited = {};
  let sizes = [];

  for (let i = 0; i < nodes.length; i++) {
    let stack = [nodes[i]];

    if (!visited[nodes[i]]) {
      let size = 0;
      while (stack.length > 0) {
        let current_node = stack.pop();

        visited[current_node] = true;
        size += 1;
        graph[current_node].forEach((node) => {
          if (!visited[node]) stack.push(node);
        });
      }
      sizes.push(size);
      connection_count += 1;
    }
  }

  sizes.sort();
  return sizes[sizes.length - 1];
};

const graph = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1],
  9: [10, 11],
  10: [9],
  11: [9],
};

console.log(connected_component_count(graph));
