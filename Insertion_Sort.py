arr=[2,3,1,4,6,5]

for i in range(1,len(arr)):
    arrI=arr[i]
    j=i-1
    while j>=0 and arr[j]>arrI:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=arrI

print(arr)