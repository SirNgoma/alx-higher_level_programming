#!/usr/bin/node

const add = (a, b) => {
  const result = a + b;
  console.log(result);
};

const arg1 = process.argv[2];
const arg2 = process.argv[3];

const integer1 = parseInt(arg1);
const integer2 = parseInt(arg2);

if (!isNaN(integer1) && !isNaN(integer2)) {
  add(integer1, integer2);
} else {
  console.log("Invalid input. Please provide two integers as arguments.");
}

