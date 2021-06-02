#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (typeof myArgs[0] === 'undefined' || isNaN(myArgs[0])) {
  console.log('Missing size');
} else {
  let myStr = '';
  for (let i = 0; i < myArgs[0]; i++) {
    myStr += 'X';
  }
  for (let i = 0; i < myStr.length; i++) {
    console.log(myStr);
  }
}
