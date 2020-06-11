""" 
kattis textencryption problem
Author: Agis Daniels
solve basically they give you the solution in this one you just need to do as asked
NOTE 

"""
from sys import stdin as rf
import collections

def solve(s, n):
    lim=len(s)
    ans=['a']*lim
    ind=0
    sta=0
    for c in range(lim):
        ans[ind]=s[c]
        ind+=n
        if ind>=lim:
            sta+=1
            ind=sta%lim
    print(''.join(ans))

def main():
    while True:
        n=int(rf.readline().strip())
        if n==0:
            return
        s=rf.readline().upper().split()
        solve(''.join(s),n)
main()
