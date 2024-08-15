package string_check_test

import (
    "go_exercises/src/string_check"
    "testing"

    . "github.com/onsi/ginkgo"
    . "github.com/onsi/gomega"
)

func TestStringCheck(t *testing.T) {
    RegisterFailHandler(Fail)
    RunSpecs(t, "StringCheck Suite")
}

var _ = Describe("Example test:", func() {
    It("Should work for fixed tests", func() {
        Expect(string_check.IsEndingWithString("", "")).To(Equal(true))
        Expect(string_check.IsEndingWithString(" ", "")).To(Equal(true))
        Expect(string_check.IsEndingWithString("abc", "c")).To(Equal(true))
        Expect(string_check.IsEndingWithString("banana", "ana")).To(Equal(true))
        Expect(string_check.IsEndingWithString("a", "z")).To(Equal(false))
        Expect(string_check.IsEndingWithString("", "t")).To(Equal(false))
        Expect(string_check.IsEndingWithString("$a = $b + 1", "+1")).To(Equal(false))
        Expect(string_check.IsEndingWithString("    ", "   ")).To(Equal(true))
        Expect(string_check.IsEndingWithString("1oo", "100")).To(Equal(false))
    })
})
