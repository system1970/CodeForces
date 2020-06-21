# https://codeforces.com/problemset/problem/122/A
# Lucky Division

n = int(input())
state = True
luckies = [4,7,47,74,447,474,477,774,747,744]
for i in range(1,n+1):
    if n%i==0 and i in luckies:
        print("YES")
        state = False
        break
if(state):
    print("NO")