# https://codeforces.com/problemset/problem/677/A
# Vanya and Fence

def solve(arr,w):
    count = 0
    for i in arr:
        if i&gt;w:
            count+=2
        else:
            count+=1
    return count
n,w = list(map(int,input().split()))
arr = list(map(int,input().split()))
print(solve(arr,w))
