""" 
kattis timeloop problem
Author: Agis Daniels
Solve print a count up from 1
NOTE 
"""
from sys import stdin as rf
def main():
    n=int(rf.readline().strip())
    for i in range(1, n+1):
        print("{} Abracadabra".format(i))
if __name__=='__main__':
    main()
