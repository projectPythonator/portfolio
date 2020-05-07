""" 
kattis t9spelling problem
Author: Agis Daniels
Solve use the layout to convert to the answer 
NOTE 
the dictionary is just a keyboard phone mapping
"""
from sys import stdin as rf
import string

mapping={}
mapping[' ']=str(0)
mapping['a']=str(2)
mapping['b']=str(22)
mapping['c']=str(222)
mapping['d']=str(3)
mapping['e']=str(33)
mapping['f']=str(333)
mapping['g']=str(4)
mapping['h']=str(44)
mapping['i']=str(444)
mapping['j']=str(5)
mapping['k']=str(55)
mapping['l']=str(555)
mapping['m']=str(6)
mapping['n']=str(66)
mapping['o']=str(666)
mapping['p']=str(7)
mapping['q']=str(77)
mapping['r']=str(777)
mapping['s']=str(7777)
mapping['t']=str(8)
mapping['u']=str(88)
mapping['v']=str(888)
mapping['w']=str(9)
mapping['x']=str(99)
mapping['y']=str(999)
mapping['z']=str(9999)

def solve(s, caseNum):
    ans='Case #{}: '.format(caseNum)
    for c in s:
        if ans[-1]==mapping[c][0]:
            ans+=' '
            ans+=mapping[c]
        else:
            ans+=mapping[c]
    print(ans)

def main():
    n=int(input())
    for i in range(n):
        s=input()
        solve(s, i+1)

if __name__=='__main__':
    main()
