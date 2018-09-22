
mm = nn = 20
cache_grid1=[[0 for i in range(nn+1)] for j in range(mm+1)]

cache_grid2=[[0 for i in range(nn+1)] for j in range(mm+1)]
'''
//long count_ways(int m, int n)
//returns the count from a recursive version
//param m and n which equal to x and y
//return 1 if we hit an edge otherwise sum of both
'''
def count_ways(n, m):
  if n == 0 or m == 0:
    return 1
  else:
    return count_ways(m-1, n)+count_ways(m, n-1)

def sol1(n, m):
  print('there are {} through a {}x{} grid'.format(count_ways(n, m), n, m))

'''
//long count_ways2(int m, int n)s
//returns the count from a recursive version by divide and conqur
//param m and n are used for the cache
//return 1 if we hit edge retrun catch pos if already known otherwise calc the spot
'''
def count_ways2(n, m):
  global cache_grid1
  if n == 0 or m == 0:
    return 1
  elif 0 < cache_grid1[m][n]:
    return cache_grid1[m][n]
  else:
    cache_grid1[m][n] = count_ways2(m, n-1)+count_ways2(m-1, n)
    return cache_grid1[m][n]

def sol2(n, m):
  print('there are {} through a {}x{} grid'.format(count_ways2(n, m), n, m))

'''
//long count_ways3(int m, int n)
//returns the count from a iterative version by divide and conqur
//param m and n are used for the grid cords
//return the answer after doing iteration
'''
def count_ways3(m, n):
  global cache_grid2
  for i in range(m+1):
    cache_grid2[i][0] = 1
  for i in range(n+1):
    cache_grid2[0][i] = 1
  for i in range(1, m+1):
    for j in range(1, n+1):
      cache_grid2[i][j] = cache_grid2[i-1][j] + cache_grid2[i][j-1]
  return cache_grid2[m][n]

def sol3(n, m):
  print('there are {} through a {}x{} grid'.format(count_ways3(m, n), n, m))

'''
//long Combinatorial_sol(int n)
//returns the count using Combinatorial
//param n is the size of the grid
//return the anser
'''
def count_ways4(n):
  res = 1
  for i in range(1, n + 1):
    res = res * (n+i)//i
  return res

def sol4(n, m):
  print('there are {} through a {}x{} grid'.format(count_ways4(n), n, m))



def main():
  #sol1(20, 20)
  sol2(20, 20)
  sol3(20, 20)
  sol4(20, 20)
main()
