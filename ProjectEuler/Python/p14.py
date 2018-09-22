max_value = 1000000
counts = [0]*max_value

def get_len(col_num):
  counter = 0
  while 1 < col_num:
    if 1 == col_num%2:
      col_num = col_num * 3 + 1
      counter += 1
    col_num //= 2
    counter += 1
  return counter

def sol1(lim):
  max_len = max_num = 0
  for col in range(1, lim+1, 2):
    cur_len = get_len(col)
    if max_len < cur_len:
      max_num = col
      max_len = cur_len
  print('the number which produces the longest chain under {} is {}'.format(lim, max_num))

def iter_proc(col_num):
  counter = 0
  while max_value <= col_num:
    if 1 == col_num%2:
      col_num = col_num * 3 + 1
      counter += 1
    col_num //= 2
    counter += 1
  return counter+next_num(col_num)

def next_num(num):
  if num >= max_value:
    return iter_proc(num)
  if 0 == counts[num - 1]:
    if 1 == num%2:
      counts[num-1] = 1 + next_num(num*3 + 1)
    else:
      counts[num-1] = 1 + next_num(num // 2)
  return counts[num-1]

def sol2(lim):
  ''' dynamic solution '''
  max_num = max_len = 0
  counts[0] = 1
  for col in range(1, lim+1, 2):
    cur_len = next_num(col)
    counts[col-1] = cur_len
    if max_len < cur_len:
      print(col)
      max_num = col
      max_len = cur_len

  print('the number which produces the longest chain under {} is {}'.format(lim, max_num))

def main():
  sol1(max_value)
  sol2(max_value)
main()
