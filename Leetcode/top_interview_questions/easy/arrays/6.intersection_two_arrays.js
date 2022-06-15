// Given two integer arrays nums1 and nums2, return an array of their intersection.
// Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */

var intersect = function (nums1, nums2) {
  let frequency_1 = {};

  // 1. get the frequency of each digit in first array
  for (let i in nums1) {
    let item = frequency_1[nums1[i]];
    item = item ? item + 1 : 1;
    frequency_1[nums1[i]] = item;
  }

  // 2. loop through the second array and decrease the frequency in frequency counter as they match
  // push items to result array
  let result = [];
  for (let i in nums2) {
    let item = nums2[i];

    if (frequency_1[item]) {
      frequency_1[item] = frequency_1[item] - 1;
      result.push(parseInt(item));
    }
  }

  return result;
};

console.log(intersect([4, 9, 5], [9, 4, 9, 8, 4]));
// console.log(intersect([1, 2, 2, 1], [2, 2]));

// 1. get the frequency of each digit in first array
// 2. loop through the second array and decrease the frequency in frequency counter as they match
// push items to result array
