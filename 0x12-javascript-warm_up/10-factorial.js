#!/user/bin/node
const factorial = (n) => {
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

const arg = process.argv[2];
const integer = parseInt(arg);

const result = factorial(integer);
console.log(result);

