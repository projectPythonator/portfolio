""" 
kattis oddities problem
Author: Agis Daniels
Solve read in n lines and test if each is odd or even
NOTE 
"""

from sys import stdin as rf
def main():
    mp={True:'even',False:'odd'}
    n=int(rf.readline())
    for line in rf:
        x=int(line)
        print("{} is {}".format(x, mp[x%2==0]))
if __name__=='__main__':
    main()
