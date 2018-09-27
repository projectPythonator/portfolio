
#author agis daniels
#Evaluate the sum of all the amicable numbers under 10000.
from math import sqrt

def sum1(n):
  return 1 + sum([i for i in range(2, n-1) if 0 == n%i])

def sum2(n):
  if 0 == n:
    return 0
  ans = step = 1
  f = 2
  lim = int(sqrt(n))
  if lim*lim == n:
    ans += lim
    lim -= 1
  if 0 != n%2:
    f = 3
    step = 2
  for i in range(f, lim+1, step):
    if 0 == n%i:
      ans += i + (n//i)
  return ans

def sum3(n):
  ans = 1
  p = 2
  if 0 == n%p:
    j = p*p
    n //= p
    while 0 == n%p:
      j *= p
      n //= p
    ans *= j-1
    ans //= p-1
  if 2 == p:
    p = 3
  while p*p <= n and 1 < n:
    if 0 == n%p:
      j = p*p
      n //= p
      while 0 == n%p:
        j *= p
        n //= p
      ans *= j-1
      ans //= p-1
    p += 2
  if 1 < n:
    ans *= n + 1
  return ans

def helper3(n):
  return sum3(n) - n

def sol1(n):
  tot = 0
  for a in range(1, n):
    print(a)
    for b in range(a+1, n):
      if helper3(b) == a and helper3(a) == b:
        tot += a + b
  return tot

def sol2(n):
  tot = 0
  for a in range(2, n):
    b = helper3(a)
    if b>a:
      if helper3(b) == a:
        tot += a + b
  return tot

def main():
  #print("the answer from sol one is {}".format(sol1(9999)))
  print("the answer from sol two is {}".format(sol2(9999)))
main()
