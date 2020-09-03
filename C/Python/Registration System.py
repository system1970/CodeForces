# https://codeforces.com/problemset/problem/4/C
# Registration System

n = int(input())
names= []
hash_map = {}
for i in range(n):
    names.append(input())
for i in names:
    if i in hash_map:
        print(i+str(hash_map[i]))
        hash_map[i]+=1
    else:
        print("OK")
        hash_map[i]=1
    