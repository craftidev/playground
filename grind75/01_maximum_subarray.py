# https://leetcode.com/problems/maximum-subarray/description/

"""
Given an integer array nums,
find the subarray with the largest sum,
and return its sum.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach,
which is more subtle.

"""
from typing import List
import unittest
import random


def maxSubArray(self, nums: List[int]) -> int:

    # O(n^2) solution
    # if len(nums) > 1:
    #     for i in range(1, len(nums)):
    #         if sum(nums[i * -1:]) < 0:
    #             return maxSubArray(self, nums[:i * -1])
    #         elif sum(nums[:i]) < 0:
    #             return maxSubArray(self, nums[i:])

    # return sum(nums)

    max_sub_array: List[int]
    for element in nums:
        if not max_sub_array:
            max_sub_array.append(element)
            continue







# Testing
class TestMaxSubArray(unittest.TestCase):
    def test_one_element_subarray(self):
        random_int = random.randint(-104, 104)
        self.assertEqual(maxSubArray(self, [random_int]), random_int)
    def test_verified_subarray(self):
        self.assertEqual(maxSubArray(self, [-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(maxSubArray(self, [5,4,-1,7,8]), 23)

if __name__ == '__main__':
    unittest.main()