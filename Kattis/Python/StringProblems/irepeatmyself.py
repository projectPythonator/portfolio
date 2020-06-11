""" 
kattis irepeatmyself problem
Author: Agis Daniels
Solve so the idea here is we use the given string as the pattern and make
a super string of each prefix and multiply it by the orginal string len
this allows us to just check if the string perdiod exists with kmp
NOTE 
since this problem we are bound n<200 and each line has at most 70 characters 
this O(n^3) time complexity passes
some optimizations like only useing sizes divisable by len(n) and maybe useing
a suffix array might improve runtime if inputs are larger
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
        self.B=[0]*(self.m+1)
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
    for line in rf:
        break
    for line in rf:
        cur=line[:-1]
        STR_CUR=STR_ALGOS()
        STR_CUR.kmpPreprocess(cur)
        worked=False
        for i in range(1, len(cur)):
            tmp=cur[:i]*len(cur)
            STR_CUR.prepKMP(tmp)
            ans=STR_CUR.kmpSearch()
            if ans:
                worked=True
                print(i)
                break
        if not worked:
            print(len(cur))
main()
