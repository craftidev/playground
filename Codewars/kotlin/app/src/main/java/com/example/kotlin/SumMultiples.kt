package com.example.kotlin
import org.junit.Test
import org.junit.Assert.*

/*
https://www.codewars.com/kata/514b92a657cdc65150000006/train/kotlin

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5
below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net
*/

fun sumOfMultiplesBelow(threshold: Int): Int {
    val multiples: Array<Int> = arrayOf(3, 5) // Don't put zero in there
    var result = 0

    if (threshold >= 0) {
        for (i in 1 until threshold) {
            for (multiple in multiples) {
                if (i % multiple == 0) {
                    result += i
                    break // Only count `i` once in case it has other multiples
                }
            }
        }
    }

    return result
}

class TestExample {
    @Test
    fun testFixed() {
        assertEquals(23, sumOfMultiplesBelow(10))
        assertEquals(78, sumOfMultiplesBelow(20))
        assertEquals(9168, sumOfMultiplesBelow(200))
    }
}
