""" 
kattis keytocrypto problem
Author: Agis Daniels
Solve step by step you undo the cipher gaining more each time
NOTE 
mci and mic , map char to int and map int to char useful for these type of 
problems
"""
from sys import stdin as rf
import string

mci={i:ord(i)-65 for i in string.ascii_uppercase}
mic={i:chr(i+65) for i in range(26)}

def unshift(a,b):
    return (mci[a]-mci[b])%26

def decrypt(c,k):
    return ''.join([mic[unshift(c[i], k[i])] for i in range(len(k))])

def solve(C,K):
    beg=K
    while len(K)<len(C):
        res=decrypt(C,K)
        K=beg+res
    lim=min(len(K), len(C))
    ans=''.join([mic[unshift(C[i], K[i])] for i in range(lim)])
    print(ans)

def main():
    C=rf.readline().strip()
    K=rf.readline().strip()
    solve(C,K)

if __name__=='__main__':
    main()
