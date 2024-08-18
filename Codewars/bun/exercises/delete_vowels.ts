/*
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
*/

function deleteVowels(string: string): string {
    const vowels = new Set(['a', 'i', 'u', 'e', 'o']);
    let result: string = '';

    string.split('').forEach((char) => {
        if (!vowels.has(char.toLowerCase())) {
            result += char;
        }
    })

    return result;
}


if (require.main === module) {
    console.log("THIS IS A NORMAL RUN - to run tests: `bun mocha exercises/file-name.ts`");
} else {
    // Tests
    const chai = require('chai');
    const assert = chai.assert;
    describe('maskify', function () {
        it('should return the string without vowel', function () {
            assert.equal(deleteVowels('should return the string without vowel'), 'shld rtrn th strng wtht vwl');
            assert.equal(deleteVowels('This website is for losers LOL!'), 'Ths wbst s fr lsrs LL!');
            assert.equal(deleteVowels('Nn vvwwls hhrr'), 'Nn vvwwls hhrr');
            assert.equal(deleteVowels(' weird  spaces   here    '), ' wrd  spcs   hr    ');
            assert.equal(deleteVowels(' wrd  spcs   hr    '), ' wrd  spcs   hr    ');
        });
    });
}