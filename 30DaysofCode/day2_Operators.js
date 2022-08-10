'use strict';

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
 * Complete the 'solve' function below.
 *
 * The function accepts following parameters:
 *  1. DOUBLE mealCost
 *  2. INTEGER tipPercent
 *  3. INTEGER taxPercent
 */

function solve (mealCost, tipPercent, taxPercent) {
  // Write your code here
  const totalCost = mealCost + mealCost * ((tipPercent / 100) + (taxPercent / 100));
  console.log(Math.round(totalCost));
}

function main () {
  const mealCost = parseFloat(readLine().trim());
  const tipPercent = parseInt(readLine().trim(), 10);
  const taxPercent = parseInt(readLine().trim(), 10);
  solve(mealCost, tipPercent, taxPercent);
}
