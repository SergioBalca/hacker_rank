process.stdin.resume();
process.stdin.setEncoding('ascii');

let inputStdin = '';
let inputStdinArray = '';
let inputCurrentLine = 0;

process.stdin.on('data', function (data) {
  inputStdin += data;
});

process.stdin.on('end', function () {
  inputStdinArray = inputStdin.split('\n');
  main();
});

// Reads complete line from STDIN
function readLine () {
  return inputStdinArray[inputCurrentLine++];
}

function main () {
  const i = 4;
  const d = 4.0;
  const s = 'HackerRank ';
  // Declare second integer, double, and String letiables.
  let secondInt = 0;
  let secondDouble = 0;
  let secondString = 0;
  // Read and save an integer, double, and String to your letiables.
  secondInt = parseInt(readLine());
  secondDouble = parseFloat(readLine());
  secondString = readLine();

  // Print the sum of both integer letiables on a new line.
  console.log(i + secondInt);
  // Print the sum of the double letiables on a new line.
  console.log((d + secondDouble).toFixed(1));
  // Concatenate and print the String letiables on a new line
  // The 's' letiable above should be printed first.
  console.log(s + secondString);
}
