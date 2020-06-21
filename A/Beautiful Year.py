# https://codeforces.com/problemset/problem/271/A
# Beautiful Year

n = list(input())
ori = n
while(len(set(n))!=len(n) or n==ori):
    n = list(str(int(''.join(n))+1))
print(''.join(n))