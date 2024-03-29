'''def solve(n,m,k,a,b):
    cnt=0
    for i in range(n):
        if a[i]>k:
            continue
        for j in range(m):
            if a[i]+b[j]<=k:
                cnt+=1
    return cnt


if __name__=='__main__':
    for _ in range(int(input())):
        n,m,k=list(map(int,input().split()))
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(solve(n,m,k,a,b))'''

def doi(n):
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
            return True
    return False
    

if __name__=='__main__':
    for _ in range(int(input())):
        # n=5
        # a=[1,3,5,5,2]
        n=int(input())
        a=list(map(int,input().split()))
        if solve(n,a):
            print('YES')
        else:
            print('NO')