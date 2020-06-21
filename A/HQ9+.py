# https://codeforces.com/problemset/problem/133/A
# HQ9+

string = list(input())
state = False
for i in string:
    if i=='H' or i=='Q' or i=="9":
        print("YES")
        state = True
        break
if state==False:
    print("NO")