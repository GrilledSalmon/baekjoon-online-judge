// 10179 쿠폰 221106 브론즈 3
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
const T = Number(input[0]);
for (let i=1; i < T+1; i++) {
  const res = Number(input[i]) * 4/5
  console.log('$'+res.toFixed(2));
}