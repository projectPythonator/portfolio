from math import sqrt
import time


def sol1(amt):
  way = [0]*(amt+1)
  way[0] =1
  for i in range(1, amt):
    for j in range(i, amt+1):
      way[j] += way[j-i]
  print('The ways to sum up to {} is {}'.format(amt, way[amt]))

  
def main():
  lim = 100
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))



main()
