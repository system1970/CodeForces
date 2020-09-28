# https://codeforces.com/problemset/problem/1409/A
# Yet Another Two Integers Problem

def solve(a1,b1):
    ans = 0
    a = max(a1,b1)
    b = min(a1,b1)
    if (a-b)%10!=0:
        ans+=1
    print((a-b)//10+ans)
        
    
for i in range(int(input())):
    a,b =list(map(int,input().split()))
    solve(a,b)

#........