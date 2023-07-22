#!/usr/bin/node
// Check if there is at least one argument (excluding the script name itself)
if (process.argv.length < 3) {
  console.log("Usage: node script_name.js <argument>");
} else {
  // Get the first argument passed to the script
  const firstArgument = process.argv[2];
  
  // Print the first argument
  console.log("First argument:", firstArgument);
}
