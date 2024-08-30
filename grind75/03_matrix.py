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
from typing import List
import unittest

class Solution:
    def binary_matrix_to_proximity_to_zero_map(
        self,
        binary_matrix_input: List[List[int]]
    ) -> List[List[int]]:

        # Init matrix output
        init_cell_value: int = -1
        proximity_map_result: List[List[int]] = [[init_cell_value] * len(row) for row in binary_matrix_input]

        # Get all the zeros
        list_of_zeros_coordinates: List[tuple] = []
        for row in range(len(binary_matrix_input)):
            for col in range(len(binary_matrix_input[row])):
                if binary_matrix_input[row][col] == 0:
                    list_of_zeros_coordinates.append((row, col))

        possible_directions: List[tuple] = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for zero_origin_row, zero_origin_col in list_of_zeros_coordinates:
            proximity_map_result[zero_origin_row][zero_origin_col] = 0

        self.breath_first_search_proximity_calculator(
            binary_matrix_input,
            proximity_map_result,
            list_of_zeros_coordinates,
            possible_directions,
            init_cell_value
        )

        return proximity_map_result

    def breath_first_search_proximity_calculator(
            self,
            matrix_input: List[List[int]],
            matrix_output: List[List[int]],
            origins: List[tuple],
            directions: List[tuple],
            default_and_unique_value: int,
            counter: int = 0
    ):
        new_origins: List[tuple] = []

        for origin_row, origin_col in origins:
            for direction_row, direction_col in directions:
                if (
                    0 <= origin_row + direction_row < len(matrix_input) and
                    0 <= origin_col + direction_col < len(matrix_input[origin_row + direction_row]) and
                    matrix_output[origin_row + direction_row][origin_col + direction_col] == default_and_unique_value
                ):
                    matrix_output[origin_row + direction_row][origin_col + direction_col] = counter + 1
                    new_origins.append((origin_row + direction_row, origin_col + direction_col))

        if new_origins:
            self.breath_first_search_proximity_calculator(
                matrix_input,
                matrix_output,
                new_origins,
                directions,
                default_and_unique_value,
                counter + 1
            )

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
