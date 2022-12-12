/**
 * @param {number[]} nums
 */
var Solution = function (nums) {
  // store digits with their indices in object
  let temp = {};
  for (let i = 0; i < nums.length; i++) {
    temp[i] = nums[i];
  }

  this.indices = temp;
  this.numbers = nums;
};

/**
 * Resets the array to its original configuration and return it.
 * @return {number[]}
 */
Solution.prototype.reset = function () {
  this.numbers = [];

  for (let i in this.indices) {
    this.numbers[i] = this.indices[i];
  }

  return this.numbers;
};

/**
 * Returns a random shuffling of the array.
 * @return {number[]}
 */
Solution.prototype.shuffle = function () {
  for (let i = 0; i < this.numbers.length; i++) {
    let random = Math.round(Math.random() * (this.numbers.length - 1 - i) + i);
    let temp = this.numbers[i];
    this.numbers[i] = this.numbers[random];
    this.numbers[random] = temp;
  }

  return this.numbers;
};

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */

const example = new Solution([1, 2, 3, 45, 32]);

console.log(example.shuffle());
console.log(example.reset());
console.log(example.shuffle());
console.log(example.shuffle());
console.log(example.reset());
