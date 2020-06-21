# https://codeforces.com/problemset/problem/705/A
# Hulk

def solve(n):
    ans = "I hate that "
    for i in range(2,n):
        if i%2==0:
           ans+="I love that "
        else:
            ans+="I hate that "
    if n%2==0:
        ans+="I love it"
    else:
        ans+="I hate it"
    return ans
            
           
n = int(input())
if n!=1:
    print(solve(n))
else:
    print("I hate it")
