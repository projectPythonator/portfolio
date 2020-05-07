""" 
kattis runlengthencodingrun problem
Author: Agis Daniels
Solve basic compression problem test cases give it away
NOTE 
mci and mic , map char to int and map int to char useful for these type of 
problems
"""
from sys import stdin as rf
import string

mci={i:ord(i)-65 for i in string.ascii_uppercase}
mic={i:chr(i+65) for i in range(26)}

def encode(s):
    ans=""
    cur=s[0]
    amt=0
    for i in s:
        if cur!=i:
            ans+=cur
            ans+=str(amt)
            amt=1
            cur=i
        else:
            amt+=1
    ans+=cur
    ans+=str(amt)
    print(ans)

def decode(s):
    ans=""
    for i in range(0,len(s),2):
        ans+=(s[i]*int(s[i+1]))
    print(ans)

def solve(op,s):
    if op=='E':
        encode(s)
    else:
        decode(s)

def main():
    op,s=rf.readline().strip().split()
    solve(op,s)

if __name__=='__main__':
    main()
