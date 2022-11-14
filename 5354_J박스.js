// 5354 J박스 221115 브론즈 3
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const T = Number(input[0]);

for (let i=1; i<T+1; i++) {
  const J = Number(input[i]);
  for (let j=0; j<J; j++) {
    let line = '';
    if (j === 0 || j === J-1) {
      line = '#'.repeat(J);
    } else {
      if (J === 1) {
        line = '#';
      } else {
        line = '#' + 'J'.repeat(J-2) + '#';
      }
    }
    console.log(line);
  }
  if (i !== T) {
    console.log();
  }
}