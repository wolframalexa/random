if __name__ == '__main__':
  xy = list(map(int, input().split()))

  grid = []
  for i in range(0,xy[0]):
    temp = list(input())
    temp.remove(' ')
    grid.append(temp)
    if 'C' in grid[i]:
      cy = grid[i].index('C')
      cx = i
  print(grid)

  rloc = grid[0].index('R')

  if rloc == xy[1]:
    print('no')

  elif True:
    posx = 0
    for i in grid:
      if i[rloc+1] == 'X':
        posx += 1
    if posx == 4:
      print('no')

  else:
    seen = [[cx, cy]]
    queue = grid
    prev = ' '
    while prev != 'R' and :
      node = queue.pop(0)

      if node not in seen:
        seen.append(node)
        neighbours = grid[node]

        for neighbour in neighbours:
          queue.append(neighbour)
    return 


