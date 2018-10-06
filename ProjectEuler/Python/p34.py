from math import factorial

num_to_fact = {}
def fill_dict():
  global num_to_fact
  for i in range(10):
    num_to_fact[str(i)] = factorial(i)

def sol1(lim):
  ans = []
  strs = list(map(str, range(10, lim)))
  for num, string in enumerate(strs, 10):
    if num == sum([num_to_fact[i] for i in string]):
      ans.append(num)
  print('sum of all nums that digit factorials sum to it self is {}'.format(sum(ans)))

def sol2(lim):
  list_num_facts = [factorial(i) for i in range(10)]
  ans = 0
  for i in range(10, lim):
    tmp_sum = 0
    tmp_num = i
    while tmp_num > 0:
      d = tmp_num % 10
      tmp_num //= 10
      tmp_sum += list_num_facts[d]
    if tmp_sum == i:
      ans += i
  print('sum of all nums that digit factorials sum to it self is {}'.format(ans))  

def main():
  lim = 2540160
  fill_dict()
  sol1(lim)
  sol2(lim)
main()
    
