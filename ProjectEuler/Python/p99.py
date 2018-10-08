
import time
from math import log10

def sol3(name_of_file):
  nums = [[int(num) for num in line.split(',')] for line in open(name_of_file).readlines()]
  ans = [[log10(nums[i][0])*nums[i][1],i+1] for i in range(len(nums))]
  ans.sort()
  print('largest number in file is {}'.format(ans[-1][1]))

def sol4(name_of_file):
  nums = [[int(num) for num in line.split(',')] for line in open(name_of_file).readlines()]
  ans = [[log10(nums[i][0])*nums[i][1],i+1] for i in range(len(nums))]
  print('largest number in file is {}'.format(max(ans)))



def main():
  name_of_file = 'in.txt'
  a = time.clock()
  sol4(name_of_file)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
  name_of_file = 'in.txt'
  a = time.clock()
  sol3(name_of_file)
  b = time.clock()
  print('time taken is {:f}'.format(b-a))
main()
