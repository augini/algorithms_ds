// Number 1
function hourglassSum(arr) {
  let sum_list = [];

  for (let i = 0; i < arr.length - 2; i++) {
    for (let n = 0; n < arr[i].length - 2; n++) {
      let top = arr[i][n] + arr[i][n + 1] + arr[i][n + 2];
      let middle = arr[i + 1][n + 1];
      let bottom = arr[i + 2][n] + arr[i + 2][n + 1] + arr[i + 2][n + 2];
      let sum = top + middle + bottom;
      sum_list.push(sum);
    }
  }

  return Math.max(...sum_list);
}

var myGrid = [
  [1, 1, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 0],
  [0, 0, 2, 4, 4, 0],
  [0, 0, 0, 2, 0, 0],
  [0, 0, 1, 2, 4, 0],
];

console.log(hourglassSum(myGrid));
