""" 
kattis encodedmessage problem
Author: Agis Daniels
Solve just transofrm to matrix rotate90 degrees then transform back 
NOTE 
we use a nice implace rotator function here
"""
from sys import stdin as rf
import string

def rotate90(mat, n):
    for i in range(n//2):
        k=n-1-i
        for j in range(i, n-i-1):
            l=n-1-j
            tmp=mat[i][j]
            mat[i][j]=mat[j][k]
            mat[j][k]=mat[k][l]
            mat[k][l]=mat[l][i]
            mat[l][i]=tmp
    
def solve(s):
    n=int(len(s)**0.5)
    mat=[list(s[i:i+n]) for i in range(0, len(s), n)]
    rotate90(mat, n)
    ans=''.join([''.join(i) for i in mat])
    print(ans)

def main():
    n=int(rf.readline().strip())
    for line in rf:
        solve(line.strip())

if __name__=='__main__':
    main()
