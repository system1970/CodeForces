# https://codeforces.com/problemset/problem/136/A
# Presents

def solve(arr):
    out = [0 for i in range(len(arr)+1)]
    for i in range(len(arr)+1):
        try:
            out[arr[i-1]] = i
        except:
            print(arr[i])
    out.pop(0)
    print(*out)
    
testcases = 1
for i in range(testcases):
    n = int(input())
    arr = list(map(int,input().split()))
    solve(arr)