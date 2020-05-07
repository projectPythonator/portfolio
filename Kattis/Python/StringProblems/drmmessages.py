""" 
kattis drmmessages problem
Author: Agis Daniels
Solve you are given instructions following them solves the problem 
NOTE 
mci and mic , map char to int and map int to char useful for these type of 
problems
"""
from sys import stdin as rf
import string

mci={i:ord(i)-65 for i in string.ascii_uppercase}
mic={i:chr(i+65) for i in range(26)}

def step1(s):
    return (s[:len(s)//2], s[len(s)//2:])

def applysum(s):
    sc=sum([mci[c] for c in s])
    return ''.join([mic[(mci[c]+sc)%26] for c in s])

def step2(a,b):
    return (applysum(a), applysum(b))

def step3(a,b):
    return ''.join([mic[(mci[a[i]]+mci[b[i]])%26] for i in range(len(a))])
    
def solve(s):
    a,b=step1(s)
    a,b=step2(a,b)
    ans=step3(a,b)
    print(ans)

def main():
    c=rf.readline().strip()
    solve(c)

if __name__=='__main__':
    main()
