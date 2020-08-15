# https://codeforces.com/problemset/problem/486/A
# Calculating Function

import math
def solve(n):
    if n%2!=0:
        print("-",end="")
    print(math.ceil(n/2))
n = int(input())
solve(n)