# https://leetcode.com/problems/01-matrix/description/

"""
With a binary matrix, return matrix of integer
-> cell int value = shortest distance to a `0` from the input matrix
ex:
Input: mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]
Output: [
    [0,0,0],
    [0,1,0],
    [1,2,1]
]
"""
from collections import deque
from math import inf
from typing import List
import unittest

class Solution:
    def binary_matrix_to_proximity_to_zero_map(
        self,
        binary_matrix_input: List[List[int]]
    ) -> List[List[int]]:

        # Init matrix output
        LARGE_NUMBER = 10**4 # equal infinity in this usecase
        proximity_map_result: List[List[int]] = [[LARGE_NUMBER] * len(row) for row in binary_matrix_input]
        input_row_count = len(binary_matrix_input)

        # Get all the zeros and add them to the queue
        search_queue = deque()
        for row in range(input_row_count):
            for col in range(len(binary_matrix_input[row])):
                if binary_matrix_input[row][col] == 0:
                    proximity_map_result[row][col] = 0
                    search_queue.append((row, col))

        possible_directions: List[tuple] = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # Breath Frist Search algorythm
        while search_queue:
            row, col = search_queue.popleft()

            for direction_row, direction_col in possible_directions:
                new_row, new_col = row + direction_row, col + direction_col

                if (
                    0 <= new_row < input_row_count and
                    0 <= new_col < len(binary_matrix_input[new_row]) and
                    proximity_map_result[new_row][new_col] > proximity_map_result[row][col] + 1
                ):
                    proximity_map_result[new_row][new_col] = proximity_map_result[row][col] + 1
                    search_queue.append((new_row, new_col))

        return proximity_map_result

# Testing
class TestMaxSubArray(unittest.TestCase):
    def protocol(
            self,
            binary_matrix_input: List[List[int]],
            expected_result: List[List[int]]
        ):
        result = Solution().binary_matrix_to_proximity_to_zero_map(binary_matrix_input)
        self.assertEqual(
            result,
            expected_result,
            msg=f"\n# Failed with matrix_input={binary_matrix_input} \
                \n# got result={result} \
                \n# expected={expected_result}"
        )
    def test_some_basics(self):
        self.protocol(
            [[0,0,0],[0,1,0],[0,0,0]],
            [[0,0,0],[0,1,0],[0,0,0]]
        )
        self.protocol(
            [[0,0,0],[0,1,0],[1,1,1]],
            [[0,0,0],[0,1,0],[1,2,1]]
        )


if __name__ == '__main__':
    unittest.main()
