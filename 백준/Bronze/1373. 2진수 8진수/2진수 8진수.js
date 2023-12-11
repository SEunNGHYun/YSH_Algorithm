const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = "";

readline
  .on("line", function (line) {
    input = line;
    readline.close();
  })
  .on("close", function () {
    //이 안에 솔루션 코드 작성
    let result = "";
    while (input.length >= 3) {
      result = parseInt(input.slice(input.length - 3), 2).toString(8) + result;
      input = input.slice(0, input.length - 3);
    }
    result = (input ? parseInt(input, 2).toString(8) : "") + result;
    console.log(result);
    process.exit();
  });
