/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
  // 1. First transpose the array, meaning swap the elements diagonally
  for (let i = 0; i < matrix.length; i++) {
    for (let m = i + 1; m < matrix[0].length; m++) {
      if (matrix[m][i] !== null) {
        let temp = matrix[m][i];
        matrix[m][i] = matrix[i][m];
        matrix[i][m] = temp;
      }
    }
  }

  // 2. Second, starting from the first array, swap the first element with the last element and second with the second last pattern
  for (let i = 0; i < matrix.length; i++) {
    for (let m = 0; m < Math.floor(matrix[i].length / 2); m++) {
      let swapIndex = matrix[i].length - (m + 1);

      let temp = matrix[i][m];
      matrix[i][m] = matrix[i][swapIndex];
      matrix[i][swapIndex] = temp;
    }
  }

  return matrix;
};

console.log(
  rotate([
    [24, 4, 38, 2, 21, 18, 33, 40],
    [24, 37, 25, 62, 37, 15, 35, 36],
    [42, 23, 13, 58, 17, 26, 19, 8],
    [32, 48, 9, 58, 36, 18, 40, 61],
    [23, 16, 0, 46, 35, 34, 23, 60],
    [9, 49, 60, 47, 1, 32, 20, 45],
    [56, 34, 40, 11, 61, 60, 20, 30],
    [45, 30, 25, 18, 49, 3, 16, 10],
  ])
);

// 1. First transpose the array, meaning swap the elements diagonally
// 2. Second, starting from the first array, swap the first element with the last element and second with the second last pattern
