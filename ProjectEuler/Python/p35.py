from math import sqrt
from math import log10
import time

circ_primes = set()
prime_set = set()
def gen_bit_sieve(lim):
  lim2 = lim // 2
  r = int(sqrt(lim)-1)//2
  bit_sieve = [False]*lim2
  bit_sieve[0] = True
  for i in range(1, r+1):
    if not bit_sieve[i]:
      for j in range(i*(i+1)+i*(i+1), lim2, 2*i+1):
        bit_sieve[j] = True
  return bit_sieve

def gen_sieve(lim):
  bit_sieve = gen_bit_sieve(lim)
  sieve = [2] + [i+i+1 for i in range((lim//2)-1) if not bit_sieve[i]]
  return sieve

def rotate1(n, dig):
  return (n%10)*(10**dig) + (n//10)

def rotate2(n):
  return n[-1] + n[:-1]

def check(a):
  dig = len(a)
  tmp = ['']*dig
  tmp[0] = a
  for i in range(1, dig):
    a = rotate2(a)
    if a in prime_set:
      tmp[i] = a
    else:
      return tmp
  return tmp

def sol1(lim):
  global prime_set, circ_primes

  siv = gen_sieve(lim)
  sieve = list(map(str, siv))
  prime_set = set(sieve)
  for i in sieve:
    if i not in circ_primes:
      possible = check(i)
      if possible[-1] != '':
        for j in possible:
          circ_primes.add(j)
  print('there are {} circular primes below one million'.format(len(circ_primes)))


def main():
  a = time.clock()
  lim = 1000000
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()

'''  for i in sieve:
    if i not in circ_primes:
      possible = check(i)
      if possible[-1] != '':
        for j in possible:
          circ_primes.add(j)
  print('there are {} circular primes below one million'.format(len(circ_primes)))'''
