const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = 0;

readline
  .on("line", function (line) {
    input = Number(line);
    readline.close();
  })
  .on("close", function () {
    //이 안에 솔루션 코드 작성
    if (input === 1) {
      console.log(4);
    } else {
      console.log(input + 3 + 3 + (input - 2) * 3);
    }
    process.exit();
  });
