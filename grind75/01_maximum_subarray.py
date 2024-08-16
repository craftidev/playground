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


def subArrayFromListAndIndexes(list: List[int], index_start: int, index_end: int) -> List[int]:
    """
    This function performs a slicing operation on a given list.

    Parameters:
    list (List[int]): The input list on which the slicing operation will be performed.
    index_start (int): The starting index for the slicing operation.
    index_end (int): The ending index for the slicing operation.

    Returns:
    List[int]: The subarray of the input list, or an empty list if the indexes are invalid.

    Raises:
    None

    Note:
    - The function performs error handling for invalid indexes, such as negative indexes, indexes greater than the list length, or an inversion of indexes.
    - The magic_operation variable is used to calculate the length of the sliced portion based on the provided indexes.
    """

    # Error handling
    if  index_start < 0          or \
        index_end   < 0          or \
        index_start >= len(list) or \
        index_end   >= len(list) or \
        index_start > index_end:
            print(
                "Error using slicing operation with indexes:",
                index_start,
                index_end,
                "-> too small or too big for list length of:",
                len(list),
                "or inversion of indexes."
            )
            return []
    #

    magic_operation = (len(list) - index_end + 1) * 1
    return list[index_start:magic_operation]


def maxSubArray(self, nums: List[int]) -> int:

##### O(n^2) solution
    #
    # if len(nums) > 1:
    #     for i in range(1, len(nums)):
    #         if sum(nums[i * -1:]) < 0:
    #             return maxSubArray(self, nums[:i * -1])
    #         elif sum(nums[:i]) < 0:
    #             return maxSubArray(self, nums[i:])

    # return sum(nums)
#####

    sum_max_subarray: int = -105 # reboot value
    potential_threshold_val: int = 0
    temporary_sum_max_subarray: int = -104 # min value

    for element in nums:
        # Init or new search after getting `temporary_sum_max_subarray`
        if sum_max_subarray == -105:
            sum_max_subarray = element
            continue

        # Find first positive number, or better negative number
        if sum_max_subarray < 0 and sum_max_subarray < element:
            sum_max_subarray = element
            continue

        # Positive encounter
        if element >= 0:
            # after a negative streak
            if potential_threshold_val < 0:
                # element bigger than negative streak
                if element + potential_threshold_val > 0:
                    sum_max_subarray += element + potential_threshold_val
                    potential_threshold_val = 0
                # element smaller than negative streak
                else:
                    potential_threshold_val += element
            # after a positive streak
            else:
                sum_max_subarray += element
        # Negative encounter
        else:
            potential_threshold_val += element
            # threshold is getting to big
            if potential_threshold_val + sum_max_subarray <= 0:
                # potential best subarray
                if temporary_sum_max_subarray < sum_max_subarray:
                    temporary_sum_max_subarray = sum_max_subarray
                    sum_max_subarray = -105
                    potential_threshold_val = 0

    return max(sum_max_subarray, temporary_sum_max_subarray)




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
        self.assertEqual(maxSubArray(self, [-1, 5, -1, 3, 3, -1, 2, -2, 5, -4, -5, -5, 20, -11, -9, 5, -1, 6, -2, 7, 5, 1]), 21)

if __name__ == '__main__':
    unittest.main()