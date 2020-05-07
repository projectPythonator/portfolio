""" 
kattis hissingmicrophone problem
Author: Agis Daniels
Solve given a line of input check if ss in in that string 
NOTE 
"""

from sys import stdin as rf
def main():
    ans=('ss' in rf.readline())
    if ans:
        print('hiss')
    else:
        print('no hiss')
if __name__=='__main__':
    main()
