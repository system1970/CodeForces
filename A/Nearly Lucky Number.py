# https://codeforces.com/problemset/problem/110/A
# Nearly Lucky Number

n = list(input())
count = 0
for i in n:
    if i=='4' or i=='7':
        count+=1
if count==4 or count==7:
    print("YES")
else:
    print("NO")