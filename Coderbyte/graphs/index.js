const graph = {
  a: ["b", "c"],
  b: ["d"],
  c: ["e"],
  d: ["f"],
  e: [],
  f: [],
};

// depth first traversal - iteratively
const depth_first_iterative = (graph, start) => {
  const visited = {};
  const stack = [start];

  while (stack.length > 0) {
    const current_node = stack.pop();
    visited[current_node] = true;
    graph[current_node].forEach((node) => stack.push(node));
  }

  return visited;
};

// depth first traversal - recursively
const depth_first_recursively = (graph, stack, visited) => {
  if (stack.length === 0) return;

  let current_node = stack.pop();
  visited[current_node] = true;
  graph[current_node].forEach((node) => stack.push(node));

  depth_first_recursively(graph, stack, visited);

  return visited;
};

// depth first traversal - recursively second way - this one by tutorial
const depth_first_recursively_2 = (graph, start, visited) => {
  visited[start] = true;

  graph[start].forEach((node) =>
    depth_first_recursively_2(graph, node, visited)
  );
  return visited;
};

// console.log(depth_first_recursively_2(graph, "a", {}));

// breadth first traversal - iteratively
const breadth_first_iterative = (graph, start) => {
  const visited = {};
  const queue = [start];

  while (queue.length > 0) {
    const current_node = queue.shift();
    visited[current_node] = true;
    graph[current_node].forEach((node) => queue.push(node));
  }

  return visited;
};

// console.log(depth_first_iterative(graph, "a"));
// console.log(breadth_first_iterative(graph, "a"));
