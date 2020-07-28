# https://codeforces.com/problemset/problem/61/A
# Ultra-Fast Mathematician

def solve():
    a = list(input())
    b = list(input())
    for i in range(len(a)):
        if a[i]!=b[i]:
            print(1,end="")
        else:
            print(0,end="")

solve()