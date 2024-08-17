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
    """
    This function finds the subarray with the largest sum in a given list of integers.
    It uses a dynamic programming approach with a time complexity of O(n).

    Parameters:
    nums (List[int]): The input list of integers.

    Returns:
    int: The sum of the subarray with the largest sum.
    """
##### O(n^2) - first solution
    # if len(nums) > 1:
    #     for i in range(1, len(nums)):
    #         if sum(nums[i * -1:]) < 0:
    #             return maxSubArray(self, nums[:i * -1])
    #         elif sum(nums[:i]) < 0:
    #             return maxSubArray(self, nums[i:])
    #
    # return sum(nums)
#####
    # Rework for a big O complexity of O(n)
    current_sum_max_subarray: int = -105 # reboot value
    negative_streak_val: int = 0
    stored_sum_max_subarray: int = -104 # min value

    for element in nums:
        # Init search
        if current_sum_max_subarray == -105:
            current_sum_max_subarray = element
            continue

        # Find first positive number, or better negative number
        if current_sum_max_subarray < 0 and current_sum_max_subarray < element:
            current_sum_max_subarray = element
            continue

        # Positive encounter
        if element >= 0:
            # after a negative streak
            if negative_streak_val < 0:
                negative_streak_val += element
                # element bigger than negative streak
                if negative_streak_val > 0:
                    current_sum_max_subarray += negative_streak_val
                    negative_streak_val = 0
            # after a positive streak
            else:
                current_sum_max_subarray += element
        # Negative encounter
        else:
            negative_streak_val += element
            # threshold is getting to big
            if negative_streak_val + current_sum_max_subarray <= 0:
                # potential best subarray
                if stored_sum_max_subarray < current_sum_max_subarray:
                    stored_sum_max_subarray = current_sum_max_subarray
                    current_sum_max_subarray = -105
                    negative_streak_val = 0

    return max(current_sum_max_subarray, stored_sum_max_subarray)

# Testing
class TestMaxSubArray(unittest.TestCase):
    def test_only_negative_int(self):
        self.assertEqual(maxSubArray(self, [-2, -101, -3, -104, -103, -2, 0, -5, -4]), 0)
    def test_one_element_subarray(self):
        random_int = random.randint(-104, 104)
        self.assertEqual(maxSubArray(self, [random_int]), random_int)
    def test_verified_subarray(self):
        self.assertEqual(maxSubArray(self, [-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(maxSubArray(self, [5, 4, -1, 7, 8]), 23)
    def test_complex_subarray(self):
        self.assertEqual(
            maxSubArray(self, [-1, 5, -1, 3, 3, -1, 2, -2, 5, -4, -5, -5, 20, -11, -9, 5, -1, 6, -2, 7, 5, 1]), 21
        )

if __name__ == '__main__':
    unittest.main()
