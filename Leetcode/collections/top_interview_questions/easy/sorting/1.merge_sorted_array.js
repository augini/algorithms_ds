/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

var merge = function (nums1, m, nums2, n) {
  let pointer_1 = m - 1;
  let pointer_2 = n - 1;

  for (let i = m + n - 1; i >= 0; i--) {
    if (nums1[pointer_1] >= nums2[pointer_2] && pointer_1 >= 0) {
      nums1[i] = nums1[pointer_1];
      pointer_1 = pointer_1 - 1;
    } else if (pointer_2 >= 0) {
      nums1[i] = nums2[pointer_2];
      pointer_2 = pointer_2 - 1;
    }
  }

  return nums1;
};

console.log(merge([0], 0, [1], 1));
