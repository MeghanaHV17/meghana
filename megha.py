arr=[]
n=int(input("Enter the number of element for array:"))
for i in range(n):
    element=int(input("Enter the element:"))
    arr.append(element)
print(element)
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    mid_element=arr[mid]
    if mid_element==key:
        print("key found at index",mid)
        break
    elif key<mid_element:
        high=mid-1
    else:
        low=mid+1
    
