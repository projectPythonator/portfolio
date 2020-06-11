""" 
kattis tolower problem
Author: Agis Daniels
solve kind of a cheesy problem but still trivial 
NOTE 

"""
from sys import stdin as rf

def main():
    P, T = map(int, input().split())
    ans = 0
    for i in range(P):
        passed = 0
        for j in range(T):
            cur = input()
            curL = cur[0].lower()+cur[1:]
            if cur[1:].lower() == curL[1:]:
                passed+=1
        if passed == T:
            ans += 1
    print(ans)
main()
