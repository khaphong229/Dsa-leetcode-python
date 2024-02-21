n=[5,3,2,7,8,1,2]

for i in range(len(n)):
    minIndex=i
    for j in range(i+1,len(n)):
        if n[j]<n[minIndex]:
            minIndex=j
    if minIndex!=i:
        temp=n[i]
        n[i]=n[minIndex]
        n[minIndex]=temp
print(n)