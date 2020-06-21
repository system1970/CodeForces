# https://codeforces.com/problemset/problem/1030/A
# In Search of an Easy Problem

def solve(arr):
    if 1 in arr:
        return "HARD"
    return "EASY"
    
n = list(map(int,input().split()))
arr = list(map(int,input().split()))
print(solve(arr))
