// 16673 고려대학교에는 공식 와인이 있다 221107 브론즈 3
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");
const [C, K, P] = input.map((e) => Number(e));
let ans = 0;
for (let c=1; c<=C; c++) {
  ans += K*c + P*c**2;
}
console.log(ans);