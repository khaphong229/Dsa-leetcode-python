'''def doi(n):
    if str(n)==str(n)[::-1]:
        return True
    return False

def chuoi(a):
    noi=''
    for i in a:
        if i!=0:
            noi+=str(i)
    return noi

def solve(n,a):
    check=0
    j=n-2
    i=1
    b=[x for x in a]
    while i<=j:
        a[i-1]=a[i-1]-1
        a[i]=a[i]-2
        a[i+1]=a[i+1]-1
        if doi(chuoi(a)):
            b=[x for x in a]
            a=[i for i in b]
            i=1
        else:
            a=[i for i in b]
            i+=1
        if len(set(b))==1 and 0 in set(b):
            check=1
            break
    if check==1:
        return True
    else:
        return False
    '''

import sys
def solve(n,a):
    j=n-1
    for i in range(1,j):
        a[i]=a[i]-(a[i-1]*2)
        a[i+1]-=a[i-1]
        if a[i] < 0 or a[i+1]<0:
            return False
        a[i-1]=0
    if len(set(a))==1 and 0 in set(a):
        return True
    return False
    
if __name__=='__main__':
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        if solve(n,a):
            print('YES')
        else:
            print('NO')