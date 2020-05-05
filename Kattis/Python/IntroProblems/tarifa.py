""" 
kattis tarifa problem
Author: Agis Daniels
Solve 
NOTE a scan as input comes in to get data build up
"""
from sys import stdin as rf
def main():
    x=int(rf.readline().strip())
    n=int(rf.readline().strip())
    ans=x
    for line in rf:
        ans=ans-int(line.strip())+x
    print(ans)
if __name__=='__main__':
    main()
