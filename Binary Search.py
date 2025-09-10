def binarysearch(l,T):
  n=len(l)
  i=0
  j=n-1
  while i<=j:
    m=(i+j)//2
    if L[m]==T:
      print(m)
      break
    elif (L[m]<T):
      i+=1 
    else:
      j-=1 
L=list(map(int,input().split( )))
T=int(input())
l=sorted(L)
binarysearch(l,T)