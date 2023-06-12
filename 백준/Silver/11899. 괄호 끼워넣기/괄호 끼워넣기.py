import sys

input = sys.stdin.readline

bracket = input().strip()

bracket_pair_check = [bracket[0]]


for i in range(1, len(bracket)):
  if bracket_pair_check and bracket_pair_check[-1] == '(' and bracket[i] == ')' : 
    bracket_pair_check.pop()
  else:
    bracket_pair_check.append(bracket[i])
    
print(len(bracket_pair_check))