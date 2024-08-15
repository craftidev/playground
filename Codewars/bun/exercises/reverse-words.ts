/*
Complete the function that accepts a string parameter,
and reverses each word in the string.
All spaces in the string should be retained.
Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
*/

function reverseWords(str: string): string {
    const wordList: string[] = str.split(' ');
    let stringBuilder: string[] = new Array<string>;

    wordList.forEach(word => {
        stringBuilder.push(word.split('').reverse().join(''));
    });


    return stringBuilder.join(' ');
}

if (require.main === module) {
    console.log("THIS IS A NORMAL RUN - to run tests: `bun mocha exercises/file-name.ts`");
} else {
    // Tests
    const chai = require('chai');
    const assert = chai.assert;
    describe('reverseWords', function () {
        it('should reverse words', function () {
            assert.equal(reverseWords('Go for it!'), 'oG rof !ti');
        });

        it('should conserve multiple spacing', function () {
            assert.equal(reverseWords('two spaces  here!'), 'owt secaps  !ereh');
            assert.equal(reverseWords('     random   crazy  spaces '), '     modnar   yzarc  secaps ');
        });
    });
}

