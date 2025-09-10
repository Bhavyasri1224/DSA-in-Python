def interpolation(arr,target):
  low=0
  high=len(arr)-1
  while low<=high and target>=arr[low] and target<=arr[high]:
    if low<=high:
      if arr[low]==target:
        return low
  
    pos=int(low+((target-arr[low])*(high-low))//(arr[high]-arr[low]))
    if pos<low or pos>high:
      return -1
    elif arr[pos]==target:
      return pos
    elif arr[pos]<target:
      high=pos-1
    else:
      low=pos+1 
  return -1
arr=list(map(int,input().split(",")))
target=int(input())
result=interpolation(arr,target)

if result==-1:
  print("Element not found")
else:
  print(result)