from math import factorial
import time

digits = [i*i for i in range(10)]
seen = {}
seen_ans = {}

def square(x):
    return int(x) * int(x)

def happy(number):
    return sum(map(square, list(str(number))))

def get_chain_len(n):
  global seen_ans, seen
  if n in seen_ans:
    return seen_ans[n]
  while True:
    n = seen[n] if n in seen else happy(n)
    if n == 89:
      return True
    elif n in seen_ans:
      return seen_ans[n]
    elif n == 1:
      return False

def sol1(lim):
  global seen_ans
  ans = 0
  for i in range(1, lim):
    tmp = get_chain_len(i)
    if i not in seen_ans:
      seen_ans[i] = tmp      
    if tmp:
      ans += 1
  print('number of chains below {} that contian 60 reapeted elms is {}'.format(lim, ans))

def main():
  lim = 10000000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))


main()
