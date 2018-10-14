from math import sqrt
import time

primes = []

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
  global primes
  bit_sieve = gen_bit_sieve(lim)
  sieve = [2] + [i+i+1 for i in range((lim//2)-1) if not bit_sieve[i]]
  primes = sieve

def euler_phi(n):
  ind = 0
  PF = primes[ind]
  ans = n
  while PF*PF <= n:
    if n%PF == 0:
      ans -= ans//PF
    while n%PF == 0:
      n//=PF
    ind += 1
    PF = primes[ind]
  if n!= 1:
    ans -= ans // n
  return ans

def sol1(lim):
  ans = best = 0
  for n in range(2, lim):
    tmp = euler_phi(n)
    if best < (n/tmp):
      best = n/tmp
      ans = n

  print('the highest phi value below {} is {}'.format(lim, ans))

def sol2(lim):
  nums = ((n/euler_phi(n), n) for n in range(2, lim))
  ans = max(nums)
  print('the highest phi value below {} is {}'.format(lim, ans))
  print(lim, ans[1]+2)



def main():
  lim = 1000000
  a = time.clock()
  gen_sieve(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
  a = time.clock()
  sol2(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))  
main()
