# https://codeforces.com/problemset/problem/734/B
# Anton and Digits

def solve(arr):
    ans = 0
    ans += (256 * min(arr[0],arr[2],arr[3]))
    arr[0] -= min(arr[0],arr[2],arr[3])
    arr[2] -= min(arr[0],arr[2],arr[3])
    arr[3] -= min(arr[0],arr[2],arr[3])
    ans += (32 * min(arr[0],arr[1]))
    return ans
    
arr = list(map(int,input().split()))
print(solve(arr))
