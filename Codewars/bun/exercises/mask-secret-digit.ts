/*
Usually when you buy something, you're asked whether your credit card number,
phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want that shown on your screen.
Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.
Examples (input --> output):

"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "####################################man!"
*/

function maskify(cc: string): string {
    const charLength: number = cc.length;

    if (charLength <= 4) {
        return cc;
    } else {
        const mask: string = '#'.repeat(charLength - 4);
        const fourLastDigit: string = cc.slice(-4).toString();

        return mask + fourLastDigit;
    }
}

if (require.main === module) {
    console.log("THIS IS A NORMAL RUN - to run tests: `bun mocha file-name.ts`");
} else {
    // Tests
    const chai = require('chai');
    const assert = chai.assert;
    describe('maskify', function () {
        it('should mask for more than 4 digit', function () {
            assert.equal(maskify('4556364607935616'), '############5616');
            assert.equal(maskify('11111'), '#1111');
        });

        it('should NOT mask for less than 4 digit', function () {
            assert.equal(maskify('1'), '1');
            assert.equal(maskify('1244'), '1244');
        });
    });
}
