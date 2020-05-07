""" 
kattis falsesecurity problem
Author: Agis Daniels
Solve make a morse code like transformation
NOTE 
"""
from sys import stdin as rf
import string
codes={'.':'---.', '_':"..--",  ',':".-.-",  '?':"----", 'A':'.-', 'B':"-...",  'C':"-.-.",  'D':"-..",  'E':".",  'F':"..-.",  'G':"--.",  'H':"....",  'I':"..",  'J':".---",  'K':"-.-",  'L':".-..",  'M':"--",  'N':"-.",  'O':"---",  'P':".--.",  'Q':"--.-",  'R':".-.",  'S':"...",  'T':"-",  'U':"..-",  'V':"...-",  'W':".--",  'X':"-..-",  'Y':"-.--",  'Z':"--.."}
rcodes={'---.':'.', "..--":'_',  ".-.-":',',  "----":'?', '.-':'A', "-...":'B',  "-.-.":'C',  "-..":'D',  ".":'E', "..-.":'F',  "--.":'G', "....":'H',  "..":'I',  ".---":'J',  "-.-":'K',  ".-..":'L',  "--":'M',  "-.":'N',  "---":'O',  ".--.":'P',  "--.-":'Q',  ".-.":'R',  "...":'S', "-":'T',  "..-":'U',  "...-":'V', ".--":'W', "-..-":'X', "-.--":'Y', "--..":'Z'}

def solve(s):
    ns=[codes[c] for c in s]
    nl=[len(w) for w in ns]
    tmp=''.join(ns)
    tmp=tmp[::-1]
    si=[c for c in tmp]
    ans=''
    while len(si)>0:
        lim=nl.pop()
        tmpStr=''
        for i in range(lim):
            tmpStr+=si.pop()
        ans+=rcodes[tmpStr]
    print(ans)
    
def main():
    for line in rf:
        s=line.rstrip()
        solve(s)

if __name__=='__main__':
    main()
