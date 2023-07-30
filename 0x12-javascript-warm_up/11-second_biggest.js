#!/usr/bin/node
const findBiggestInteger = (...args) => {
  if (args.length === 0) {
    return 0;
  } else if (args.length === 1) {
    return 0;
  } else {
    let biggest = parseInt(args[0]);
    for (let i = 1; i < args.length; i++) {
      const currentInt = parseInt(args[i]);
      if (!isNaN(currentInt) && currentInt > biggest) {
        biggest = currentInt;
      }
    }
    return biggest;
  }
};

const argList = process.argv.slice(2);
const biggestInteger = findBiggestInteger(...argList);
console.log(biggestInteger);
