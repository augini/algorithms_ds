// Takes a sorted array and returns the index of the value if it exists, otherwise -1
const binarySearch = (sortedArr, value) => {
  let left = 0;
  let right = sortedArr.length - 1;

  while (left < right) {
    let middle = Math.floor((left + right) / 2);
    if (value === sortedArr[middle]) {
      return middle;
    } else if (value > sortedArr[middle]) {
      left = middle;
    } else if (value < sortedArr[middle]) {
      right = middle;
    }
  }

  return -1;
};

console.log(
  binarySearch(
    [2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24],
    1
  )
);
