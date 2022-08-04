#!/usr/bin/node

/**
 * Morse code challenge.
 * Program that is able to convert regular text into Morse code and viceversa.
 * In Morse code line "-", dot ".", one space between letter, and two spaces "  " between words, are supported.
 */

// Object to convert regular text into Morse code.

const alphabetMorse = {
  a: '.- ',
  b: '-... ',
  c: '-.-. ',
  d: '-.. ',
  e: '. ',
  f: '..-. ',
  g: '--. ',
  h: '.... ',
  i: '.. ',
  j: '.--- ',
  k: '-.- ',
  l: '.-.. ',
  m: '-- ',
  n: '-. ',
  o: '--- ',
  p: '.--. ',
  q: '--.- ',
  r: '.-. ',
  s: '... ',
  t: '- ',
  u: '..- ',
  v: '...- ',
  w: '.-- ',
  x: '-..- ',
  y: '-.-- ',
  z: '--.. ',
  1: '.---- ',
  2: '..--- ',
  3: '...-- ',
  4: '....- ',
  5: '..... ',
  6: '-.... ',
  7: '--... ',
  8: '---.. ',
  9: '----. ',
  0: '----- ',
  ' ': '  '
};

// Object created to convert Morse code into regular text.

const morseAlphabet = {
  '.-': 'a',
  '-...': 'b',
  '-.-.': 'c',
  '-..': 'd',
  '.': 'e',
  '..-.': 'f',
  '--.': 'g',
  '....': 'h',
  '..': 'i',
  '.---': 'j',
  '-.-': 'k',
  '.-..': 'l',
  '--': 'm',
  '-.': 'n',
  '---': 'o',
  '.--.': 'p',
  '--.-': 'q',
  '.-.': 'r',
  '...': 's',
  '-': 't',
  '..-': 'u',
  '...-': 'v',
  '.--': 'w',
  '-..-': 'x',
  '-.--': 'y',
  '--..': 'z',
  '.----': 1,
  '..---': 2,
  '...--': 3,
  '....-': 4,
  '.....': 5,
  '-....': 6,
  '--...': 7,
  '---..': 8,
  '----.': 9,
  '-----': 0,
  '  ': ' '
};

function decoder (inputString) {
  let str = '';

  if (inputString[0] in alphabetMorse) {
    for (const element of inputString) {
      if (element in alphabetMorse) {
        str += alphabetMorse[element];
      } else {
        return ('Invalid input');
      }
    }
  } else if (inputString[0] in morseAlphabet) {
    inputString.split('  ').map(e => e.split(' ')).map(e => e.map(element => {
      if (element in morseAlphabet) {
        str += morseAlphabet[element];
      } else {
        return ('Invalid Morse code');
      }
      return (str);
    }));
  }

  return (str);
}

console.log(decoder('-- -.--   -. .- -- .   .. ...   ... . .-. --. .. ---'));

/* console.log(decoder('-- -.--  -. .- -- .  .. ...  ... . .-. --. .. ---')); */
