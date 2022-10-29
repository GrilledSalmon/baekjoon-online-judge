// 221029(토) 10569 다면체 브론즈 3
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const T = Number(input[0]);
for (let i = 0; i < T; i++) {
  const [V, E] = input[i+1].split(' ');
  console.log(2-Number(V)+Number(E));
}