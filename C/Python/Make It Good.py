# https://codeforces.com/problemset/problem/1385/C
# Make It Good

for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = len(arr)-1
    while ans&gt;0 and arr[ans-1]&gt;=arr[ans]:
        ans-=1
    while ans&gt;0 and arr[ans-1]&lt;=arr[ans]:
        ans-=1
    print(ans)