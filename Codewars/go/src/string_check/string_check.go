/*
Complete the solution so that it returns true if
the first argument (string) passed in ends with the 2nd argument (also a string).

Examples:

solution("abc", "bc") // returns true
solution("abc", "d") // returns false
*/

package string_check

import (
    "reflect"
)

func IsEndingWithString(str string, ending string) bool {
    rune_str := []rune(str)
    rune_ending := []rune(ending)

    return  len(rune_str) >= len(rune_ending) &&
            reflect.DeepEqual(
                rune_str[len(rune_str)-len(rune_ending):], rune_ending,
            )
}
