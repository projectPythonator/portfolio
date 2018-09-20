def valid_pairs(n):
  if n < 1:
    return ''
  pairs = set(['()'])
  for i in range(1, n):
    temp = set()
    for p in pairs:
      temp.add(p+'()')
      temp.add('()'+p)
      temp.add('('+p+')')
    pairs = temp
  return pairs

print(valid_pairs(20))
