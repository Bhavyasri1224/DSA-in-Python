def Exponent(arr,target):
  n=len(arr)
  if (arr[0]==target):
    return 0
  i=1 
  while i<r and arr[i]<=target:
    i=i*2
    low=i//2
    high=min(i,n-1)
  return BinarySearch(arr,target,low,high)
def BinarySearch(arr,target,low,high):
  mid=low+high//2
  if arr[mid]==target:
    return mid
  elif arr[mid]<target:
    high=mid-1
  else:
    low=mid+1