import time

def sol1(lim):
  ans = 0
  for a in range(1, lim):
    for b in range(1, lim):
      cur = sum(map(int,str(a**b)))
      if cur > ans:
        ans = cur
  print(ans)

def sol2(lim):
  ans = (sum(map(int,str(a**b))) for a in range(1, lim) for b in range(1, lim))
  print(max(ans))

def main():
  lim = 101
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
  a = time.clock()
  sol2(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
  
