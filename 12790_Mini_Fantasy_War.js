// 12790 Mini Fantasy War 221105 브론즈 3
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
T = Number(input[0]);
for (let i = 1; i < T+1; i++) {
  let [A, B, C, D, a, b, c, d] = input[i].split(' ').map((e) => Number(e));
  A = A+a < 1 ? 1 : A+a;
  B = B+b < 1 ? 1 : B+b;
  C = C+c < 0 ? 0 : C+c;
  D += d;
  console.log(A + 5*B + 2*C + 2*D);
}