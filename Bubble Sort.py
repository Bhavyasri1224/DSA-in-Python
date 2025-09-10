def bubblesort(arr,n):
  for i in range(n):
    swap=False
    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        temp=arr[j]
        arr[j]=arr[j+1]
        arr[j+1]=temp
        swap=True
    if not swap:
      break
  return arr
arr=list(map(int,input().split()))
n=len(arr)
bubblesort(arr,n)
print(*arr)