// 2903 중앙 이동 알고리즘 221104 브론즈 3
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const N = input[0];
let n = 3
for (let i=0; i<N-1; i++) {
  n = 2*(n-1)+1
}
console.log(n**2);