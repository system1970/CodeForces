# https://codeforces.com/problemset/problem/1397/A
# Juggling Letters

from sys import stdin, stdout
inp = lambda : list(map(int,stdin.readline().split()))

def solve():
    n = inp()[0]
    hash_map = {}
    for j in range(n):
        arr = list(input())
        for i in arr:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
    for i in hash_map:
        if hash_map[i]%n!=0:
            return "NO"
    return "YES"

def main():
    for i in range(inp()[0]):
        print(solve())
        

main()
