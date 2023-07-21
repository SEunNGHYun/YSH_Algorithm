let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");
let n = Number(input[0]);
let result = "";
let left = [];
let right = [];
for (let i = 1; i < n; i++) {
  left = [];
  right = [];
  for (let j = 1; j <= i; j++) {
    left.push("*");
    right.push("*");
  }
  for (let j = 1; j <= n - i; j++) {
    left.push(" ");
    right.push(" ");
  }
  result += left.join("") + right.reverse().join("") + "\n";
}
left = [];
right = [];
for (let j = 1; j <= n; j++) {
  left.push("*");
  right.push("*");
}
result += left.join("") + right.reverse().join("") + "\n";
for (let i = 1; i < n; i++) {
  left = [];
  right = [];
  for (let j = 1; j <= n - i; j++) {
    left.push("*");
    right.push("*");
  }
  for (let j = 1; j <= i; j++) {
    left.push(" ");
    right.push(" ");
  }

  result += left.join("") + right.reverse().join("") + "\n";
}

console.log(result);
