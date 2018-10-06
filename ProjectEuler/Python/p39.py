from math import sqrt
from math import gcd
import time

def sol1(lim):
  dic = {}
  pows = [i**2 for i in range(lim)]
  i = 1
  while i < lim:
    j = i+1
    while i+j < lim+1:
      ij = i+j
      k = j+1
      while ij+k < lim+1:
        if pows[i]+pows[j] == pows[k]:
          if ij+k in dic:
            dic[ij+k] += 1
          else:
            dic[ij+k] = 1
        k+=1
      j+=1
    i+=1
  ans = sorted([[v, k] for k, v in dic.items()])
  print('For which value of p ≤ 1000, is the number of solutions maximised is {}'.format(ans[-1]))

def sol2(lim):
  res = ressol = 0
  for p in range(2, lim+1, 2):
    numsol = 0
    li = p//3
    for a in range(2, li):
      if (p*(p-a+a)) % (2*(p-a)) == 0:
        numsol+=1
    if numsol>ressol:
      ressol = numsol
      res = p
  print('For which value of p ≤ 1000, is the number of solutions maximised is {}'.format(res))
  
def sol3(lim):
  pMa = tMa = m = k = 0
  for i in range(1, lim+1):
    t = 0
    mlim = int(sqrt(i//2)+1)
    for m in range(2, mlim+1):
      if m&1 != 1:
        k = m + 1
      else:
        k = m + 2
      mm = 2*m
      imm = i//mm
      while k < mm and k <= imm:
        if imm % k == 0 and gcd(k, m) == 1:
          t += 1  
        k += 2
    if t > tMa:
      tMa= t
      pMa = i
  print('For which value of p ≤ 1000, is the number of solutions maximised is {}'.format((tMa, pMa)))


def main():
  lim = 1000 
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
  a = time.clock()
  sol2(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
  a = time.clock()
  sol3(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
