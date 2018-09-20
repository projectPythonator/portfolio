
def valid_pairs(n):
    if n < 1:
        return ''
    #pairs of brackets that we will build up upon
    pairs = set(['()'])
    for i in range(1, n):
        # fill set up with the next lvl n then set pairs to that level
        temp = set()
        for p in pairs:
            temp.add(p+'()')
            temp.add('()'+p)
            temp.add('('+p+')')
        pairs = temp
    return pairs

print(valid_pairs(20))
