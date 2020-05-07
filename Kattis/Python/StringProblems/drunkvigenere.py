""" 
kattis drunkvigenere problem
Author: Agis Daniels
Solve you are given the encrypte just reverse it 
NOTE 
mci and mic , map char to int and map int to char useful for these type of 
problems
"""
from sys import stdin as rf
import string

mci={i:ord(i)-65 for i in string.ascii_uppercase}
mic={i:chr(i+65) for i in range(26)}

def applyShift(a,b,i):
    if i%2==1:
        return (a+b)%26
    else:
        return (a-b)%26
    
def solve(C,K):
    ans=''.join([mic[applyShift(mci[C[i]], mci[K[i]], i)] for i in range(len(C))])
    print(ans)

def main():
    C=rf.readline().strip()
    K=rf.readline().strip()
    solve(C,K)

if __name__=='__main__':
    main()
