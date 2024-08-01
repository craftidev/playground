// Input
function getRandomInteger(min: number, max: number): number {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const input = getRandomInteger(-99, 99);

// Force positive integer
const number = Math.abs(input);
// Binary conversion
const binaryString = number.toString(2);

console.log(`The binary representation of ${input} is ${binaryString} (negative sign is ignored)`);

// Sum all the ones by transforming the string into an array of strings
// And use reduce to add them up
const sumOfOnes = binaryString.split('').reduce((accumulator: number, currentValue: string) => {
    return accumulator + parseFloat(currentValue);
}, 0);

console.log(`The number of ones in ${binaryString} is ${sumOfOnes}`);
