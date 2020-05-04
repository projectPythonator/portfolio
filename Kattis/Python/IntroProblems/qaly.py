""" 
kattis qaly problem
Author: Agis Daniels
Solve summation of quality[i]*years[i]
"""
from sys import stdin as rf
def main():
    n=int(rf.readline().strip())
    ans=0
    for line in rf:
        q,y=map(float, line.split())
        ans+=q*y
    print("{:.3f}".format(ans))
if __name__=='__main__':
    main()
