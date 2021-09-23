const pivot = (arr) => {
  let pivotPoint = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[pivotPoint]) {
      let temp = arr[pivotPoint];
      arr[pivotPoint] = arr[pivotPoint + 1];
      arr[pivotPoint + 1] = temp;

      temp = arr[i];
      arr[i] = arr[pivotPoint];
      arr[pivotPoint] = temp;
      pivotPoint = pivotPoint + 1;
      console.log(pivotPoint);
      console.log(arr);
    }
  }

  console.log({ pivotPoint });

  return pivotPoint;
};

console.log(pivot([5, 2, 1, 8, 4, 7, 6, 3]));
