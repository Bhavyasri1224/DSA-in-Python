n=int(input())
def number(m):
  m=str(n)
  k=len(m)
  pairs={'1':'1','0':'0','8':'8','9':'6','6':'9'} 
  for i in range((k+1)//2):
    left=m[i]
    right=m[k-1-i]
    if left not in pairs or pairs[left]!=right:
      return False
    return True
if number(n):
  print("Equal")
else:
  print("Not Equal")