"""
Make a program that filters a list of strings
and returns a list with only your friends name in it.

If a name has exactly 4 letters in it,
you can be sure that it has to be a friend of yours!
Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend {"Ryan", "Kieran", "Mark"} `shouldBe` {"Ryan", "Mark"}

If there are no friends return {""}.
/!\ error in instructions, what was required to return was empty list []
added a test for it /!\

Note: keep the orig inal order of the names in the output.

"""

import codewars_test as test

def friend(input_list):
    onlyFriends = list()

    for name in input_list:
        if len(name) == 4:
            onlyFriends.append(name)

    return onlyFriends

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Sample Test Cases')
    def sample_test_cases():
        test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
        test.assert_equals(friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]), ["Ryan"])
        test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])
        test.assert_equals(friend(["ONLY_ENNEMY"]), [])