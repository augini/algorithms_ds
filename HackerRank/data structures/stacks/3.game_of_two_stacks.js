function twoStacks(maxSum, a, b) {
  let counter = 0;
  let currentSum = 0;

  while (currentSum <= maxSum && a.length && b.length) {
    if (a[0] < b[0]) {
      if (currentSum + a[0] > maxSum) break;
      console.log([a[0]]);
      currentSum += a.shift();
    } else if (b[0] < a[0]) {
      if (currentSum + b[0] > maxSum) break;
      console.log([b[0]]);
      currentSum += b.shift();
    }
    counter++;
  }

  return counter;
}

/*
 * Complete the twoStacks function below.
 */
function twoStacks(x, a, b) {
  var ai = 0,
    bi = 0;

  var ret = 0,
    total = 0,
    cnt = 0;

  while (ai < a.length && total + a[ai] <= x) {
    total += a[ai++];
  }

  while (bi < b.length && total + b[bi] <= x) {
    total += b[bi++];
  }
  console.log(total);
  console.log({ ai });
  console.log({ bi });
  ret = ai + bi;

  while (true) {
    while (ai > 0 && total + b[bi] > x) {
      total -= a[ai - 1];
      ai--;
    }
    if (total + b[bi] > x || bi >= b.length) break;
    total += b[bi++];
    ret = Math.max(ret, ai + bi);
  }
  return ret;
}

console.log(twoStacks(10, [4, 2, 4, 6, 1], [2, 1, 8, 5]));
