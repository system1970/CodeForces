# https://codeforces.com/problemset/problem/1325/B
# CopyCopyCopyCopyCopy

def solve(arr):
   return len(set(arr))
testcases = int(input())
for i in range(testcases):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(arr))
