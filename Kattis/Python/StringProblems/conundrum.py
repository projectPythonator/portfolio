""" 
kattis conundrum problem
Author: Agis Daniels
Solve a simple word transformation problem
NOTE 
"""
from sys import stdin as rf
def main():
    c=rf.readline().strip()
    ans=0
    nam=['P', 'E', 'R']
    for i in range(len(c)):
        if c[i]!=nam[i%3]:
            ans+=1
    print(ans)

if __name__=='__main__':
    main()
