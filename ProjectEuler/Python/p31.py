

coins = [1,2,5,10,20,50,100,200]

memo = []

way = []

def fill_memo_zeros(a, b):
  global memo
  memo = [[0]*b for i in range(a)]

def fill_way(a):
  global way
  way = [1]*a

def ways(targ, avc):
  if avc < 2: return 1
  res = 0
  while 0 <= targ:
    res += ways(targ, avc-1)
    targ -= coins[avc-1]
  return res

def memo_ways(targ, avc):
  global memo
  t = targ
  if avc < 2: return 1
  elif 0 < memo[t][avc-1]: return memo[t][avc-1]
  else:
    res = 0
    while 0 <= targ:
      res  += memo_ways(targ, avc-1)
      targ -= coins[avc-1]
    memo[t][avc-1] = res
    return res

def sol1(amt):
  fill_memo_zeros(amt, 8)
  ans = ways(amt, 8)
  print('The ways to sum up the coin from doing basic method {}'.format(ans))

def sol2(amt):
  fill_memo_zeros(amt+1, 8)
  ans = memo_ways(amt, 8)
  print('The ways to sum up the coin from doing memo method  {}'.format(ans))

def sol3(amt):
  global way
  fill_way(amt+1)
  for i in range(1, 8):
    c = coins[i]
    for j in range(c, amt+1):
      way[j] += way[j-c]
  print('The ways to sum up the coin from doing memo method  {}'.format(way[amt]))

def main():
  amt = 200
  sol1(amt)
  sol2(amt)
  sol3(amt)
main()
