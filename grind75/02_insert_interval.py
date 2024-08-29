# https://leetcode.com/problems/insert-interval/description/

"""
Insert an interval [start_i, end_i] in a list of intervals.
the list of intervals is sorted in ascending order by start_i.
the function merge any overlap between previous intervals and the new one.
"""
from typing import List
import unittest

class Solution:
    def insert_interval(
        self,
        intervals: List[List[int]],
        new_interval: List[int]
    ) -> List[List[int]]:

        result_intervals: List[List[int]] = [new_interval]

        if not intervals:
            return result_intervals

        for interval in intervals:
            previous_interval = result_intervals[-1:][0]
            previous_interval_ix = len(result_intervals) - 1

            if interval[0] <= previous_interval[0]:
                if  interval[1] >= previous_interval[0]:
                    result_intervals[previous_interval_ix][0] = interval[0]
                    result_intervals[previous_interval_ix][1] = max(previous_interval[1], interval[1])
                else:
                    result_intervals.insert(previous_interval_ix, interval)
            else:
                if interval[0] > previous_interval[1]:
                    result_intervals.append(interval)
                else:
                    result_intervals[previous_interval_ix][1] = max(previous_interval[1], interval[1])

        return result_intervals

# Testing
class TestMaxSubArray(unittest.TestCase):
    def protocol(
            self,
            list_test: List[List[int]],
            input_test: List[int],
            expected_result: List[List[int]]
        ):
        result = Solution().insert_interval(list_test, input_test)
        self.assertEqual(
            result,
            expected_result,
            msg=f"\n# Failed with list_test={list_test} \
                \n# input_test={input_test} \
                \n# got result={result} \
                \n# expected={expected_result}"
        )
    def test_some_basics(self):
        self.protocol(
            [[3,6], [12,14], [17,88]],
            [1,16],
            [[1,16], [17,88]]
        )
        self.protocol(
            [[1,2],[3,5],[6,7],[8,10],[12,16]],
            [4,8],
            [[1,2],[3,10],[12,16]]
        )
        self.protocol(
            [[1,3],[6,9]],
            [2,5],
            [[1,5],[6,9]]
        )
        self.protocol(
            [[1,3],[6,9]],
            [4,5],
            [[1,3],[4,5],[6,9]]
        )
        self.protocol(
            [[1,3],[6,9]],
            [7,11],
            [[1,3],[6,11]]
        )
        self.protocol(
            [[1,2],[3,5],[6,7],[8,10],[12,16]],
            [0,11],
            [[0,11],[12,16]]
        )
        self.protocol(
            [[2,4],[5,7],[8,10],[11,13]],
            [3,6],
            [[2,7],[8,10],[11,13]]
        )
        self.protocol(
            [[0,5],[9,12]],
            [7,16],
            [[0,5],[7,16]]
        )


if __name__ == '__main__':
    unittest.main()
