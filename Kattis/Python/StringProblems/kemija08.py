""" 
kattis kemija08 problem
Author: Agis Daniels
Solve rebuild the string by iterating the index correctly
NOTE 
"""
from sys import stdin as rf
import string
    
def solve(s):
    vowels=set(['a','e','i','o','u'])
    ans=''
    ind=0
    while ind<len(s):
        ans+=s[ind]
        if s[ind] in vowels:
            ind+=3
        else:
            ind+=1
    print(ans)

def main():
    s=rf.readline().strip()
    solve(s)

if __name__=='__main__':
    main()
