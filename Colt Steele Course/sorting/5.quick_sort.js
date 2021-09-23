const pivot = (arr) => {
  let pivotPoint = 0;
  let temp;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[pivotPoint]) {
      if (pivotPoint + 1 === i) {
        temp = arr[i];
        arr[i] = arr[pivotPoint];
        arr[pivotPoint] = temp;
      } else {
        temp = arr[pivotPoint];
        arr[pivotPoint] = arr[pivotPoint + 1];
        arr[pivotPoint + 1] = temp;

        temp = arr[pivotPoint];
        arr[pivotPoint] = arr[i];
        arr[i] = temp;
      }

      pivotPoint = pivotPoint + 1;
    }
  }

  return pivotPoint;
};

console.log(pivot([5, 2, 1, 8, 4, 7, 6, 3]));
