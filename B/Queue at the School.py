# https://codeforces.com/problemset/problem/266/B
# Queue at the School

def solve(queue,x):
    modded = list(queue)
    for j in range(x):
        for i in range(len(queue)-1):
            if list(queue)[i]=="B" and list(queue)[i+1]=="G":
                temp = modded[i]
                modded[i] = modded[i+1]
                modded[i+1] = temp
        queue = ''.join(modded)
    print(''.join(modded))
testcases = 1
for i in range(testcases):
    n,x = list(map(int,input().split()))
    queue = input()
    solve(queue,x)