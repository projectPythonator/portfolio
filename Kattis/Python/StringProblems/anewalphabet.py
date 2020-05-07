""" 
kattis anewalphabet problem
Author: Agis Daniels
Solve just map all the chars in the mapping to the new char while keeping old chars
the same
NOTE 
"""
from sys import stdin as rf
import string

mapping={'a':'@','n':'[]\[]','b':'8','o':'0','c':'(','p':'|D','d':'|)','q':'(,)','e':'3','r':'|Z','f':'#','s':'$','g':'6','t':"']['",'h':'[-]','u':'|_|','i':'|','v':'\/','j':'_|','w':'\/\/','k':'|<','x':'}{','l':'1','y':'`/','m':'[]\/[]','z':'2'}

def solve(s):
    ans=''
    for c in s:
        if c in mapping:
            ans+=mapping[c]
        else:
            ans+=c
    print(ans)

def main():
    s=rf.readline().strip().lower()
    solve(s)

if __name__=='__main__':
    main()
