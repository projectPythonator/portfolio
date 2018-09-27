#autoher agis daniels
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def sum_divs(n):
  ans = 1
  if 0 == n%2:
    j = 4
    n //= 2
    while 0 == n%2:
      j *= 2
      n //= 2
    ans *= (j - 1)
  p = 3
  while p*p <= n and 1 < n:
    if 0 == n%p:
      j = p*p
      n //= p
      while 0 == n%p:
        j *= p
        n //= p
      ans *= (j-1)
      ans //= (p-1)
    p += 2
  if 1<n:
    ans *= (n+1)
  return ans

def helper(n):
  return sum_divs(n) - n

def get_list(n):
  return [i for i in range(12, n+1) if i < helper(i)]

def sol1(S, L, n):
  ans = 0
  siz = len(L)
  for i in range(1, n):
    worked = True
    for j in range(siz):
      tmp = i - L[j]
      if tmp in S:
        worked = False
        break
      if tmp < 12:
        break
    if worked:
      ans += i
  return ans

def sol2(L, n):
  ans = 0
  siz = len(L)
  opp = [True]*n
  a = 0
  while L[a] + L[a] < n:
    aVal = L[a]
    tmp = aVal + aVal
    b = a + 1
    while tmp < n:
      opp[tmp] = False
      tmp = aVal + L[b]
      b += 1
    a += 1
  return sum([i for i in range(n) if opp[i]])

def main():
  n = 28123
  L = get_list(n)
  print('staart')
  print('The sum of all the numbers that cant be writen as the sum of two abundant using method of bool vec numbers is: {}'.format(sol2(L, n)))
  print('The sum of all the numbers that cant be writen as the sum of two abundant using binary scearch numbers is: {}'.format(sol1(set(L), L, n)))

if __name__=='__main__':
	main()
