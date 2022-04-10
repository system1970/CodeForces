# https://codeforces.com/problemset/problem/1660/A
# Vasya and Coins

def solve():

    a,b = list(map(int,input().split()))

    return a + 2 * b + 1 if a &gt; 0 else 1


for _ in range(int(input())):

    print(solve())