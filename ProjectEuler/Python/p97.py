
import time
from math import log10

def last_ten1(n):
  return str(n)[-10:]

def last_ten2(n):
  #leno = int((log10(n))+1
  digits = ''
  for i in range(10):
    digits += str(n % 10)
    n//=10
  return digits[::-1]

def sol1(num):
  print('last ten digits of 28433×2^7830457+1 is {}'.format(last_ten2(num)))

def main():
  num = 28433*(2**7830457)+1
  a = time.clock()
  sol1(num)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
