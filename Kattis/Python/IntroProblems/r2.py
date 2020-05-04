""" 
kattis R2 problem
Author: Agis Daniels
Solves for r2 in mean calc (r1+r2)//2 == s
"""
from sys import stdin as rf
def main():
    r,s=map(int, rf.readline().split())
    ans= s-(r-s) if r>s else s+(s-r)
    print("{}".format(ans))
if __name__=='__main__':
    main()
