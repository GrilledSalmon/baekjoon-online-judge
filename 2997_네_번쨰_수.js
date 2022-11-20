// 2997 네 번째 수 221120 브론즈 3
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
const [a, b, c] = input[0].split(" ").map((e) => Number(e)).sort((a, b) => a-b);
const d1 = b - a;
const d2 = c - b;
if (d1 === d2) {
  console.log(c + d1);
} else if (d1 > d2) {
  console.log((a + b) / 2);
} else {
  console.log((b + c) / 2);
}
