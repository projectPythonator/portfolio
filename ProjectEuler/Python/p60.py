from math import sqrt
import time

s_primes = set()
l_primes = []

seen = {}

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

def gen_bit_sieve(lim):
  lim2 = lim // 2
  r = int(sqrt(lim)-1)//2
  bit_sieve = [False]*lim2
  bit_sieve[0] = True
  for i in range(1, r+1):
    if not bit_sieve[i]:
      for j in range(2*i*(i+1), lim2, 2*i+1):
        bit_sieve[j] = True
  return bit_sieve

def gen_sieve(lim):
  global l_primes, s_primes
  bit_sieve = gen_bit_sieve(lim)
  l_primes = [i+i+1 for i in range((lim//2)-1) if not bit_sieve[i]]
  s_primes = set(l_primes)

def check(a, b):
  return (is_prime(int(a+b)))

def test(a, b):
  global seen
  aa = max(a, b)
  bb = min(a, b)
  if (aa, bb) in seen:
    return seen[(aa, bb)]
  seen[(aa, bb)] = (check(a, b) and check(b, a))
  return seen[(aa, bb)]

def sol1(lim):
  global seen
  for a in range(lim):
    aa = str(l_primes[a])
    print(aa)
    for b in range(a+1, lim):
      bb = str(l_primes[b])
      if test(aa, bb):
        for c in range(b+1, lim):
          cc = str(l_primes[c])
          if test(aa, bb) and test(bb, cc):
            for d in range(c+1, lim):
              dd = str(l_primes[d])
              if test(aa, dd) and test(bb, dd) and test(cc, dd):
                for e in range(d+1, lim):
                  ee = str(l_primes[e])
                  if test(aa, ee) and test(bb, ee) and test(cc, ee) and test(dd, ee):
                    print(sum([int(i) for i in [aa,bb,cc,dd, ee]]),aa,bb,cc,dd, ee)
                    return
  return 0


def main():
    lim = 9000
    a = time.clock()
    gen_sieve(lim)
    b = time.clock()
    print('time taken is {:f}'.format(b-a))
    lim2 = len(l_primes)
    a = time.clock()
    sol1(lim2)
    b = time.clock()
    print('time taken is {:f}'.format(b-a))
main()
