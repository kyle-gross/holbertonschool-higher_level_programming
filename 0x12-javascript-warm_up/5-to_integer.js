#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (typeof myArgs[0] === 'undefined') {
  console.log('Not a number');
} else {
  console.log('My number: %i', myArgs[0]);
}
