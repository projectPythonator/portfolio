""" 
kattis transitwoes problem
Author: Agis Daniels
Solve to check if our route allows us to arrive on time
NOTE 
"""
from sys import stdin as rf
def main():
    s,t,n=map(int, rf.readline().split())
    coms=list(map(int, rf.readline().split()))
    tims=list(map(int, rf.readline().split()))
    arvs=list(map(int, rf.readline().split()))
    for i in range(n):
        tmp=arvs[i]
        s+=coms[i]
        s+=(((tmp-(s%tmp))%tmp)+(tims[i]))
    if s+coms[n-1]<=t:
        print("yes")
    else:
        print("no")
if __name__=='__main__':
    main()
