#!/usr/bin/node

const argument = process.argv[2];

if (!isNaN(argument) && Number.isInteger(parseFloat(argument))) {
  const x = parseInt(argument);
  for (let i = 0; i < x; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
