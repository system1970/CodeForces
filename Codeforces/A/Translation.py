# https://codeforces.com/problemset/problem/41/A
# Translation

a = "".join(reversed(input())) 
b = input()
if a==b:
    print("YES")
else:
    print("NO")