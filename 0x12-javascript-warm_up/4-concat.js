#!/usr/bin/node
// Check if there are exactly two arguments
if (process.argv.length !== 4) {
  console.log("Usage: node script_name.js <argument1> <argument2>");
} else {
  // Get the two arguments passed to the script
  const arg1 = process.argv[2];
  const arg2 = process.argv[3];
  
  // Print the arguments in the specified format
  console.log(`${arg1} is ${arg2}`);
}

