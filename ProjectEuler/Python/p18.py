
'''
//get_sum(int ind,int graph[136],int level)
//recursive solution
//params ind is the current index
//       graph is the graph we are traversing through
//       level is the level of the triangle
//return the greatest sum
'''
def get_sum(ind, graph, lvl):
  if 0 == graph[ind + lvl]:
    return graph[ind]
  else:
    return graph[ind]+max(get_sum(ind+lvl,graph,lvl+1),get_sum(ind+lvl+1,graph,lvl+1))

def sol1(graph):
  print('biggest sum path of the graph is {}'.format(get_sum(0, graph, 1)))

def my_first_sol(graph, lvls):
  set_low = [0]*lvls
  set_hgh = [0]*lvls
  set_tmp = [0]*lvls
  set_low[0] = graph[0]+graph[1]
  set_low[1] = graph[0]+graph[2]
  z = 0
  indu = hgh_lvl = 3
  while 0 != graph[indu]:
    z = 0
    for i in range(hgh_lvl):
      set_hgh[i] = graph[indu+i]
    set_tmp[0] = set_hgh[0]+set_low[z]
    for i in range(1, hgh_lvl-1):
      if set_low[z + 1] <= set_low[z]:
        set_tmp[i] = set_hgh[i] + set_low[z]
      else:
        set_tmp[i] = set_hgh[i] + set_low[z+1] 
      z += 1
    set_tmp[hgh_lvl-1] = set_hgh[hgh_lvl-1]+set_low[hgh_lvl-2]
    set_low = [i for i in set_tmp]
    indu += hgh_lvl
    hgh_lvl += 1
  return max(set_low)

def sol2(graph, lvls):
  print('biggest sum path of the graph is {}'.format(my_first_sol(graph, lvls)))

def main():
  graph = [75,95,64,17,47,82,18,35,87,10,20,4,82,47,65,19,1,23,75,3,34,88,2,77,73,7,63,67,99,65,4,28,6,16,70,92,41,41,26,56,83,40,80,70,33,41,48,72,33,47,32,37,16,94,29,53,71,44,65,25,43,91,52,97,51,14,70,11,33,28,77,73,17,78,39,68,17,57,91,71,52,38,17,14,91,43,58,50,27,29,48,63,66,4,68,89,53,67,30,73,16,69,87,40,31,4,62,98,27,23,9,70,98,73,93,38,53,60,4,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  sol1(graph)
  sol2(graph, 15)
main()
