function check(s) {
  let stack = [s[0]]
  var last = '';
  let i = 0
  for(let j = 1; j < s.length; j++) {
    last = stack[i]
    if(last == '('){
      if(s[j] == ')') {
        stack.pop()
        i -= 1
      }else{
        stack.push(s[j])
        i += 1
      }
    }else if(last == '['){
      if(s[j] == ']') {
        stack.pop()
        i -= 1
      }else{
        stack.push(s[j])
        i += 1
      }
    }
    else if(last == '{'){
      if(s[j] == '}') {
        stack.pop()
        i -= 1
      }else{
        stack.push(s[j])
        i += 1
      }
    }
    else {
      stack.push(s[j])
      i += 1
    }
    if (i < 0){
      i = -1
    }
  }
  if (stack.length > 0){
    return false
  }else{
    return true
  }
}

function solution(s){ 
  let count = 0
  for(let i = 0; i < s.length; i++){
    if(check(s)) {
      count += 1
    }
    s = s.slice(1) +  s.slice(0,1) ;
  }
  return count
}
