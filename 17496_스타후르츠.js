// 221031 17496 스타후르츠 브론즈 3
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
const [N, T, C, P] = input;
const cycle = Math.floor((N-1)/T);
console.log(cycle*C*P);