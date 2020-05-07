""" 
kattis isithalloween problem
Author: Agis Daniels
Solve simply check if its halloween or xmax
NOTE 
"""

from sys import stdin as rf
def main():
    monSet=set(['OCT 31', 'DEC 25'])
    dat=rf.readline().strip()
    if dat in monSet:
        print("yup")
    else:
        print("nope")
if __name__=='__main__':
    main()
