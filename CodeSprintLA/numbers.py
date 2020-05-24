if __name__ == '__main__':
  num = list(map(int, input().split(' ')))
  N = num[0]
  M = num[1]
  numops = 0

  explored = []
  queue = [[N]]

  if N == M:
    numops = 0
    print(numops)
    exit()

  while queue:
    path = queue.pop(0)

    neighbours = [N+1, N-1, 2*N]
    numops += 1

    for neighbour in neighbours:
       new_path = list(path)
       new_path.append(neighbour)
       queue.append(new_path)

       if new_path == M:
         print(numops)
         exit()



