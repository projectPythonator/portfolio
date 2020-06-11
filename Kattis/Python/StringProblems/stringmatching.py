""" 
kattis stringmatching problem
Author: Agis Daniels
Solve simply use the kmp algorithm to find all the indices for each case
NOTE 
time complexity is O(n+k) 
since we are only searching for one pattern suffix arrays might tle 
as they are nlogn for each case to build them 
brute force search is too slow since we could run into 10000+ size strings
"""
from sys import stdin as rf

class STR_ALGOS:
    def __init__(self):
        self.n=0
        self.T=''
    
    def prepKMP(self, s):
        self.n=len(s)
        self.T=s
    
    def kmpPreprocess(self, s):
        self.m=len(s)
        self.P=s
        self.B=[0]*(self.m+1) #add plus one if no work
        self.B[0]=j=-1
        for i in range(self.m):
            while j>=0 and self.P[i] != self.P[j]:
                j=self.B[j]
            j+=1
            self.B[i+1]=j
    
    def kmpSearch(self):
        ans=[]
        j=0
        for i in range(self.n):
            while j>=0 and self.T[i] != self.P[j]:
                j=self.B[j]
            j+=1
            if j==self.m:
                ans.append(1+i-j)
                j=self.B[j]
        return ans

def main():
    p=''
    s=''
    for i,line in enumerate(rf):
        if i%2==0:
            p=line.strip()
        else:
            s=line.strip()
            STR_SOLVE=STR_ALGOS()
            STR_SOLVE.prepKMP(s)
            STR_SOLVE.kmpPreprocess(p)
            ans=STR_SOLVE.kmpSearch()
            print(' '.join(map(str,ans)))
main()
