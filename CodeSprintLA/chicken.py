if __name__ == '__main__':
  xy = list(map(int, input().split()))

  grid = []
  for i in range(0,xy[0]):
    temp = list(input())
    temp.remove(' ')
    grid.append(temp)
  print(grid)

  rloc = grid[0].index('R')

  if rloc == xy[1]:
    print('no')

  else:
    posx = 0
    for i in grid:
      if i[rloc+1] == 'X':
        posx += 1
    if posx == 4:
      print('no')



