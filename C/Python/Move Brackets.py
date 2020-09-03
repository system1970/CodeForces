# https://codeforces.com/problemset/problem/1374/C
# Move Brackets

for i in range(int(input())):

    n = int(input())
    
    s = list(input())
    
    ans,bal =0,0
    
    for i in range(n):
        if s[i]=="(":

            bal+=1

        else:

            bal-=1

            if bal&lt;0:

                bal = 0

                ans+=1

    print(ans)
        