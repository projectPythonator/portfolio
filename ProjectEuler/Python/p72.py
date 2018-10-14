from math import gcd
import time

def sol1(lim):
  eulerPhi = [i for i in range(lim+1)]
  for i in range(2, lim+1):
    if eulerPhi[i] == i:
      for j in range(i, lim+1, i):
        eulerPhi[j] = (eulerPhi[j]/i)*(i-1)
  print('the num proper fracs bellow {} is {}'.format(lim, int(sum(eulerPhi[2:]))))


def main():
  lim = 1000000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
