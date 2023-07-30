#!/usr/bin/node
const arg = process.argv[2];

if (!isNaN(arg) && Number.isInteger(parseFloat(arg))) {
  const size = parseInt(arg);
  if (size <= 0) {
    exit;
  } else {
    for (let i = 0; i < size; i++) {
      let row = "";
      for (let j = 0; j < size; j++) {
        row += "X";
      }
      console.log(row);
    }
  }
} else {
  console.log("Missing size");
}

