from math import sqrt
import time

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

def sol1(lim):
  sieve = gen_sieve(lim)
  set_sieve = set(sieve)
  prime_sums = [0]*(len(sieve)+1)
  for i in range(len(sieve)):
    prime_sums[i+1] = prime_sums[i] + sieve[i]
  ans = 0
  leno = len(prime_sums)
  for i in range(leno):
    ii = prime_sums[i]
    for j in range(i+1, leno):
      if prime_sums[j]> lim: break
      ij = prime_sums[j]-ii
      if ij in set_sieve and ans < ij:
        ans = ij
  print('the longest consecutive prime below {} is {}'.format(lim, ans))


def sol2(lim):
  sieve = gen_sieve(lim)
  set_sieve = set(sieve)
  prime_sums = [0]*(len(sieve)+1)
  for i in range(len(sieve)):
    prime_sums[i+1] = prime_sums[i] + sieve[i]
  nump = i = ans = 0
  leno = len(prime_sums)
  while i < leno:
    j = i - (nump+1)
    ii = prime_sums[i]
    while j >= 0:
      ij = ii-prime_sums[j]
      if ij > lim: break
      elif ij in set_sieve:
        nump = i - j
        ans = ij
      j -= 1
    i += 1
  print('the longest consecutive prime below {} is {}'.format(lim, ans))



def main():
  lim = 1000000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
  a = time.clock()
  sol2(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
  
