
import time

nums = []
seen = set()

def get_chain_len(n, l):
  global seen
  if n in seen:
    return (0, 0)
  cur = []
  i = n
  broke = False
  leno = 0
  small = 0
  while i not in cur:
    cur.append(i)
    i = nums[i]
    if i > 1000000 or i in seen:
      broke = True
      break
  if not broke:
    ind =  cur.index(i) 
    if len(cur) - ind > l:
      small = min(cur[ind:])
      leno = len(cur) - ind
  for el in cur:
    seen.add(el)
  return (leno, small)

def gen_facts_sums(lim):
  r_list = [0]*(lim+1)
  for i in range(1, (lim//2)+1):
    for j in range(2*i, lim+1, i):
      r_list[j] += i
  return r_list

def sol1(lim):
  global nums
  nums = gen_facts_sums(lim)
  longest = 0
  smallest = 1000000000
  for i in range(2, lim + 1):
    leno, sml = get_chain_len(i, longest)
    if leno > longest:
      longest = leno
      smallest = sml
  print('smallest number of the longest ami chain below {} is {}'.format(lim, smallest))

def main():
  lim = 1000000
  a = time.clock()
  sol1(lim)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))


main()
