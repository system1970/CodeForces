# https://codeforces.com/problemset/problem/344/A
# Magnets

def solve():
    n =int(input())
    groups = 1
    tracker = list(input())[1]
    for j in range(n-1):
        try:
            i = list(input())
            if i[0]==tracker:
                groups+=1
            tracker = i[1]
        except Exception as e:
            print(e)
    return groups

print(solve())