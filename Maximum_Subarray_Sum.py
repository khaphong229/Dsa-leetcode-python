def solve(n,a):
    # max_val=float('-inf')
    # for i in range(n):
    #     for j in range(i,n):
    #         max_val=max(max_val,sum(a[i:j+1]))
    # return max_val
    max_val, sum_val=0,0
    for i in range(n):
        sum_val=max(a[i],sum_val+a[i])
        max_val=max(max_val,sum_val)
    return max_val
    
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    print(solve(n,a))