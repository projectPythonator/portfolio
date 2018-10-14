from math import sqrt
import time

primes = []
set_p = set()

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
  global primes, set_p
  bit_sieve = gen_bit_sieve(lim)
  sieve = [2] + [i+i+1 for i in range((lim//2)-1) if not bit_sieve[i]]
  primes = sieve
  set_p = set(primes)

def euler_phi(n):
  if n in set_p:
    return n-1
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

def is_perm(a, b):
  if len(str(a)) != len(str(b)):
    return False
  c = [0]*10
  while a > 0:
    c[a%10] += 1
    a//=10
  while b > 0:
    c[b%10] -= 1
    b//=10
  for i in c:
    if i != 0:
      return False
  return True


def sol1(lim):
  ans = best = 1000000000
  for n in range(3, lim, 2):
    tmp = euler_phi(n)
    if best > n/tmp:
      if is_perm(n, tmp):
        best = n/tmp
        ans = n
  print('the highest phi value below {} is {}'.format(lim, ans))
  
def sol2(lim):
  eulerPhi = [i for i in range(lim+1)]
  for i in range(2, lim+1):
    if eulerPhi[i] == i:
      for j in range(i, lim+1, i):
        eulerPhi[j] = (eulerPhi[j]/i)*(i-1)
  ans = 0
  best = 100000000000000000000000
  for n in range(2, lim):
    tmp = eulerPhi[n]
    if best > n/tmp:
      if is_perm(n, int(tmp)):
        best = n/tmp
        ans = n
  print('the highest phi value below {} is {}'.format(lim, ans))



def main():
  lim = 10**7
  a = time.clock()
  gen_sieve(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
  a = time.clock()
  sol2(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
