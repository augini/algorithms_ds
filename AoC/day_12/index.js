const create_adjacency_list = (map) => {
  const edges = map.split("\n");
  const adjacency_list = {};

  for (let i = 0; i < edges.length; i++) {
    const [first, second] = edges[i].split("-");
    if (!adjacency_list[first]) adjacency_list[first] = [];
    if (second !== "end" && !adjacency_list[second])
      adjacency_list[second] = [];
  }

  for (let i = 0; i < edges.length; i++) {
    const [first, second] = edges[i].split("-");
    if (!adjacency_list[first].includes(second) && second !== "start")
      adjacency_list[first].push(second);

    if (
      second !== "end" &&
      !adjacency_list[second].includes(first) &&
      first !== "start"
    )
      adjacency_list[second].push(first);
  }

  return adjacency_list;
};

// {
//   start: [ 'A', 'b' ],
//   A: [ 'c', 'b', 'end' ],
//   b: [ 'A', 'd', 'end' ],
//   c: [ 'A' ],
//   d: [ 'b' ]
// }

function getLastValue(set) {
  let value;
  for (value of set);
  return value;
}

const find_paths = (graph, start, path) => {
  const collection = [];
  const visited_small = new Set();
  const stack = [start];

  while (stack.length > 0) {
    const current_cave = stack.pop();

    // if (path[path.length - 1] === current_cave) {
    //   path = path.slice(0, 1);
    //   visited_small.clear();
    // }

    if (current_cave === current_cave.toUpperCase()) {
      // console.log(current_cave, path, stack);
      path.push(current_cave);
    } else {
      if (!visited_small.has(current_cave)) {
        path.push(current_cave);
        visited_small.add(current_cave);
      } else {
        const lastItem = path[path.length - 1];
        if (lastItem === lastItem.toLowerCase()) {
          path.pop();
        }
        continue;
      }
    }

    if (current_cave === "end") {
      // console.log(current_cave, path, stack, visited_small);
      collection.push(path.join(","));
      path.pop();
      visited_small.delete("end");
    } else {
      graph[current_cave].forEach((cave) => stack.push(cave));
    }
  }

  return collection;
};

const graph = create_adjacency_list(`dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc`);
console.log(graph);

console.log(find_paths(graph, "start", []));
