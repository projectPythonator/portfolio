""" 
kattis autori problem
Author: Agis Daniels
Solve simply just split the string on - then print the first letter of each word
NOTE 
"""
from sys import stdin as rf
def main():
    a=rf.readline().strip().split('-')
    print(''.join([i[0] for i in a]))

if __name__=='__main__':
    main()
