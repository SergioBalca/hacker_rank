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
 * Complete the 'migratoryBirds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function migratoryBirds (arr) {
  // Write your code here

  // to find frecuency of each birdId and store it in an object.

  const frecuency = {};
  for (const birdId of arr) {
    if (frecuency[birdId]) {
      frecuency[birdId] += 1;
    } else {
      frecuency[birdId] = 1;
    }
  }

  /**
   * Some browsers that not support values() method, so keys()
   * and map methods are used instead.
   */

  const values = Object.keys(frecuency).map((key) => {
    return (frecuency[key]);
  });

  // To find max value
  const max = values.reduce((a, b) => {
    return Math.max(a, b);
  }, -Infinity);

  // To get min id from values
  const minId = Object.keys(frecuency).map((key) => {
    if (frecuency[key] === max) {
      return (key);
    }
    return {};
  }).sort();
  return (minId[0]);
}

function main () {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
  const arrCount = parseInt(readLine().trim(), 10);
  const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));
  const result = migratoryBirds(arr);
  ws.write(result + '\n');
  ws.end();
}
