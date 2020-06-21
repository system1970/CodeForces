# https://codeforces.com/problemset/problem/734/A
# Anton and Danik

def solve(games):
    if games.count('D')&gt;games.count('A'):
        return "Danik"
    elif games.count('D')&lt;games.count('A'):
        return "Anton"
    return "Friendship"
n = int(input())
games = list(input())
print(solve(games))