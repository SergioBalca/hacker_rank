'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on('end', function () {
  inputString = inputString.split('\n');
  main();
});

function readLine () {
  return inputString[currentLine++];
}

/*
 * Complete the 'pangrams' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function pangrams (s) {
  // Write your code here

  const sLower = s.toLowerCase(); // to ignore upper case
  const alpha = Array.from(Array(26)).map((e, i) => i + 97); // To generate an array of 26 positions filled with Charcode
  const alphabet = alpha.map((x) => String.fromCharCode(x)); // To convert Charcode to string and generate the alphabet
  if (s.length < 26) {
    return ('not pangram');
  }

  for (const element of alphabet) {
    // To check if string has all letters from alphabet
    if (sLower.includes(element)) {
      continue;
    } else {
      return ('not pangram');
    }
  }
  return ('pangram');
}

function main () {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
  const s = readLine();
  const result = pangrams(s);
  ws.write(result + '\n');
  ws.end();
}
