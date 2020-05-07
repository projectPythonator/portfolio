""" 
kattis faktor problem
Author: Agis Daniels
Solve simple algebra solve for x given a and i type of deal
NOTE 
"""

from sys import stdin as rf
def main():
    a,i=map(int, rf.readline().split())
    print(a*(i-1)+1)
if __name__=='__main__':
    main()
