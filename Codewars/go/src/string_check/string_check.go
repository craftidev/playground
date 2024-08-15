/*
Complete the solution so that it returns true if
the first argument (string) passed in ends with the 2nd argument (also a string).

Examples:

solution("abc", "bc") // returns true
solution("abc", "d") // returns false
*/

package string_check

func IsEndingWithString(str string, ending string) bool {

    return  len(str) >= len(ending) &&
            str[len(str)-len(ending):] == ending
}
