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
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach,
which is more subtle.

"""
from typing import List
import unittest
import random

class Solution:
    # The simplest shit ever... got side tracked with that D&Q in the instructions
    def maxSubArray(self, nums: List[int]) -> int:
        current_max: int = 0
        overall_max: int = -100001 # Min val

        for num in nums:
            current_max = max(num + current_max, num)
            overall_max = max(current_max, overall_max)

        return overall_max

    #####
        # Looking at LLM D&Q solution, trying to work it out
        ######################################################
        # return self.devide_and_conquer(nums, 0, len(nums) - 1)[0]

    # def devide_and_conquer(self, nums: List[int], left: int, right: int) -> tuple[int, int, int, int]:
        # # Base case when divided down to one element
        # if left == right:
        #     return nums[left], nums[left], nums[left], nums[left]

        # # Divide -> recursion
        # mid = (left + right) // 2
        # left_result = self.devide_and_conquer(nums, left, mid)
        # right_result = self.devide_and_conquer(nums, mid + 1, right)

        # # Conquer -> max left/right/half crossing
        # max_left_right: int = max(left_result[0], right_result[0])
        # half_crossing_sum: int = left_result[2] + right_result[1]
        # current_max: int = max(max_left_right, half_crossing_sum)

        # # Combine -> 1,5 crossing becomes new left/right and new total
        # left_handed_max: int = max(left_result[1], left_result[3] + right_result[1])
        # right_handed_max: int = max(right_result[2], right_result[3] + left_result[2])
        # total_sum: int = left_result[3] + right_result[3]

        # return current_max, left_handed_max, right_handed_max, total_sum
    #####

    #####
        # O(n^2) - first solution
        ######################################################
        # if len(nums) > 1:
        #     for i in range(1, len(nums)):
        #         if sum(nums[i * -1:]) < 0:
        #             return self.maxSubArray(nums[:i * -1])
        #         elif sum(nums[:i]) < 0:
        #             return self.maxSubArray(nums[i:])
        #
        # return sum(nums)
    #####

    #####
        # First rework for a big O complexity of O(n)
        # Not working on complexe tests
        #####################################################
        # current_sum_max_subarray: int = -100001 # reboot value
        # negative_streak_val: int = 0
        # stored_sum_max_subarray: int = -10000 # min value
        #
        # for element in nums:
        #     # Init search
        #     if current_sum_max_subarray == -105:
        #         current_sum_max_subarray = element
        #         continue
        #
        #     # Find first positive number, or better negative number
        #     if current_sum_max_subarray < 0 and current_sum_max_subarray < element:
        #         current_sum_max_subarray = element
        #         continue
        #
        #     # Positive encounter
        #     if element >= 0:
        #         # after a negative streak
        #         if negative_streak_val < 0:
        #             negative_streak_val += element
        #             # element bigger than negative streak
        #             if negative_streak_val > 0:
        #                 current_sum_max_subarray += negative_streak_val
        #                 negative_streak_val = 0
        #         # after a positive streak
        #         else:[-2, 1, -3, 4, -1, 2, 1, -5, 4]
        #             current_sum_max_subarray += element
        #     # Negative encounter
        #     else:
        #         negative_streak_val += element
        #         # negative streak is getting too big
        #         if negative_streak_val + current_sum_max_subarray <= 0:
        #             # store potential best subarray
        #             if stored_sum_max_subarray < current_sum_max_subarray:
        #                 stored_sum_max_subarray = current_sum_max_subarray
        #                 current_sum_max_subarray = -100001
        #                 negative_streak_val = 0
        #
        # return max(current_sum_max_subarray, stored_sum_max_subarray)
    #####

    #####
        # 3rd try after reading about D&Q
        # Confusion, use too much memory
        #####################################################v
    # class Solution:
        # def __init__(self):
        #     self.max_cumulative_sum_left: int = 0
        #     self.max_cumulative_sum_right: int = 0
        #     self.max_subarray_sum: int = -100001
        #
        # def maxSubArray(self, nums: List[int]) -> int:
        # # Second rework with D&Q idea in mind
        #     for cursor_left in range(0, len(nums)):
        #         cursor_right: int = len(nums) - 1 - cursor_left
        #
        #         self.max_cumulative_sum_left += nums[cursor_left]
        #         self.max_cumulative_sum_right += nums[cursor_right]
        #         self.max_subarray_sum = max(
        #             self.max_subarray_sum,
        #             self.max_cumulative_sum_left,
        #             self.max_cumulative_sum_right
        #         )
        #
        #         if (cursor_left + 1) * 2 <= len(nums):
        #             if self.max_cumulative_sum_left < 0 or self.max_cumulative_sum_right < 0:
        #                 self.max_cumulative_sum_left = max(0, self.max_cumulative_sum_left)
        #                 self.max_cumulative_sum_right = max(0, self.max_cumulative_sum_right)
        #                 return self.maxSubArray(nums[cursor_left + 1:-(cursor_left + 1)])
        #
        #     return self.max_subarray_sum
    #####

# Testing
class TestMaxSubArray(unittest.TestCase):
    def test_only_negative_int(self):
        self.assertEqual(Solution().maxSubArray([-2, -101, -3, -104, -103, -2, 0, -5, -4]), 0)
    def test_one_element_subarray(self):
        random_int = random.randint(-104, 104)
        self.assertEqual(Solution().maxSubArray([random_int]), random_int)
    def test_verified_subarray(self):
        self.assertEqual(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(Solution().maxSubArray([5, 4, -1, 7, 8]), 23)
    def test_complex_subarray(self):
        self.assertEqual(
            Solution().maxSubArray([-1, 5, -1, 3, 3, -1, 2, -2, 5, -4, -5, -5, 20, -11, -9, 5, -1, 6, -2, 7, 5, 1]), 21
        )

if __name__ == '__main__':
    unittest.main()
