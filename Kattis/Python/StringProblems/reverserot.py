""" 
kattis reverserot problem
Author: Agis Daniels
Solve simple modified version of rot13 where its rotx
NOTE 
mci and mic , map char to int and map int to char useful for these type of 
problems
"""
from sys import stdin as rf
import string

mci={i:ord(i)-65 for i in string.ascii_uppercase}
mic={i:chr(i+65) for i in range(26)}
mci['_']=26
mci['.']=27
mic[26]='_'
mic[27]='.'

def shift(a,b):
    return (mci[a]+b)%28

def decrypt(s,r):
    return ''.join([mic[shift(c, r)] for c in s])

def solve(R,S):
    ans=S[::-1]
    print(decrypt(ans,R))

def main():
    for line in rf:
        if line[0]=='0':
            break
        r,s=line.strip().split()
        solve(int(r),s)

if __name__=='__main__':
    main()
