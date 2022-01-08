// 1. loop through the array in a conventional way and check for land
// 2. once land is found, start bfs search until all surrounding land has been explored

// this function takes points of the land in the grid
// and returns the points of all surrounding lands
const breadth_first_search = (points, grid) => {
  let queue = [points];

  let land_points = [];
  while (queue.length > 0) {
    const _points = queue.shift();
    land_points.push(_points);

    let [y, x] = _points.split(",");
    x = parseInt(x);
    y = parseInt(y);

    if (
      grid[y + 1] &&
      grid[y + 1][x] === "L" &&
      !land_points.includes(`${y + 1},${x}`)
    ) {
      grid[y + 1][x] = "*L";
      queue.push(`${y + 1},${x}`);
    }
    if (
      grid[y - 1] &&
      grid[y - 1][x] === "L" &&
      !land_points.includes(`${y - 1},${x}`)
    ) {
      grid[y - 1][x] = "*L";
      queue.push(`${y - 1},${x}`);
    }
    if (grid[y][x + 1] === "L" && !land_points.includes(`${y},${x + 1}`)) {
      grid[y][x + 1] = "*L";
      queue.push(`${y},${x + 1}`);
    }
    if (grid[y][x - 1] === "L" && !land_points.includes(`${y},${x - 1}`)) {
      grid[y][x - 1] = "*L";
      queue.push(`${y},${x - 1}`);
    }
  }

  return land_points;
};

const islandCount = (grid) => {
  let row_length = grid[0].length;
  let all_land = [];

  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < row_length; x++) {
      // once land is found, start bfs search with the current index
      if (grid[y][x] === "L") {
        let land_area = breadth_first_search(`${y},${x}`, grid);
        all_land.push(land_area);
      }
    }
  }

  return all_land.length;
};

const grid = [
  ["L", "L", "L"],
  ["L", "L", "L"],
  ["L", "L", "L"],
];
console.log(islandCount(grid)); // -> 3
