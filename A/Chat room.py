# https://codeforces.com/problemset/problem/58/A
# Chat room

s = list(input())
need = ['h','e','l','l','o']
count=0
for i in s:
    if i==need[0]:
        count+=1
        need.pop(0)
    if len(need)==0:
        break
if len(need)==0:
    print("YES")
else:
    print("NO")