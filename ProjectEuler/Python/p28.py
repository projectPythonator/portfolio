



def sol1(lim):
  ans  = 0
  i = 1
  step = 2
  end = (lim)*(lim)
  while i<end:
    ans  += i
    i    += step
    ans  += i
    i    += step
    ans  += i
    i    += step
    ans  += i
    i    += step
    step += 2
  print('the sum of the diagonals of {} by {} is {}'.format(lim, lim, ans+end))

def sol2(lim):
  ans = 1
  b = 2
  x = 3
  for i in range(2, (lim//2+2)):
    ans += 4*x + 6*b
    x += b*4 + 2
    b += 2
  print('the sum of the diagonals of {} by {} is {}'.format(lim, lim, ans))


def main():
  lim = 1001
  sol1(lim)
  sol2(lim)

main()
