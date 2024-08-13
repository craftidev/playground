"""
A square of squares

You like building blocks.
You especially like building blocks that are squares.
And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square.
Instead, you end up with an ordinary rectangle! Those blasted things!
If you just had a way to know, whether you're currently working in vain…
Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task:
Given an integral number, determine if it's a square number:
    In mathematics, a square number or perfect square is an integer that is the square of an integer;
    in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples:
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
"""
import codewars_test as test

def is_square_number(input: int) -> bool:
    sqrt: float = input ** 0.5
    return input >= 0 and sqrt - int(sqrt) == 0

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(is_square_number(-1), False, "-1: Negative numbers cannot be square numbers")
        test.assert_equals(is_square_number( 0), True, "0 is a square number (0 * 0)")
        test.assert_equals(is_square_number( 3), False, "3 is not a square number")
        test.assert_equals(is_square_number( 4), True, "4 is a square number (2 * 2)")
        test.assert_equals(is_square_number(25), True, "25 is a square number (5 * 5)")
        test.assert_equals(is_square_number(26), False, "26 is not a square number")
