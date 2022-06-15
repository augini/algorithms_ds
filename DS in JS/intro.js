// Time Complexity: O(1)
// Space Complexity: O(1)

/**
2 * Raise number to the power.
3 *
4 * Example:
5 * number = 3
6 * power = 2
7 * output = 3^2 = 9
8 *
9 * @param {number} number
10 * @param {number} power
11 * @return {number}
12 */

export function fastPower(number, power) {
  return number ** power;
}

// Time Complexity: O(power)
// Space Complexity: O(1)
export function iterativePower(number, power) {
  let result = 1;

  for (let i = 0; i < power; i += 1) {
    result *= number;
  }

  return result;
}
