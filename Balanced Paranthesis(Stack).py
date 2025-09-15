def para(n):
  stack=[]
  pairs={'}':'{',')':'(',']':'['}
  for i in n:
    if i in '({[':
      stack.append(i)
    elif i in ')}]':
      if stack[-1]!=pairs[i]:
        return False
      stack.pop()
  return True 
n=input()
if (para(n)):
  print("Balanced")
else:
  print("Not Balanced")