# https://codeforces.com/problemset/problem/231/A
# Team

def solve(n):
    ans = 0
    for i in range(n):
        arr = list(map(int,input().split()))
        if sum(arr)&gt;=2:
            ans+=1
    print(ans)

solve(int(input()))
