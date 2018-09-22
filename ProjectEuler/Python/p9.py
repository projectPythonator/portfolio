from math import sqrt, ceil

def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)


def sol1(lim):
  for a in range(3, (lim-3)//3):
    for b in range(a+1, (lim-1-a)//2):
      c = lim - a - b
      if c*c == b*b + a*a:
        print('the triplet where a + b + c == 1000 and a^2 + b^2 = c^2 is {}'.format(a*b*c))

def sol2(lim):
  ''' a studied solution '''
  s2 = lim//2
  mlim = int(ceil(sqrt(s2))-1)
  for m in range(2, mlim + 1):
    if 0 == s2%m:
      sm = s2//m
      while 0 == sm%2:
        sm //= 2
      k = 0
      if 1 == m%2:
        k = m + 2
      else:
        k = m + 1
      while k < m+m and k <= sm:
        if 0 == sm%k and 1 == gcd(k, m):
          d = s2 // (k*m)
          n = k-m
          a = d * (m*m - n*n)
          b = d*m*n*2
          c = d * (m*m + n*n)
          print('the triplet where a + b + c == 1000 and a^2 + b^2 = c^2 is {}'.format(a*b*c))
        k += 2

def main():
  sol2(1000)
  sol1(1000)
main()
 
