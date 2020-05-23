if __name__ == '__main__':
  num = list(map(int, input().split(' ')))
  numfac = num[0]
  numpairs = num[1]

  past = []
  all = [i for i in range(1,numfac+1)]
  depts = 0

  for i in range(0, numpairs):
    curr = list(map(int, input().split(' ')))
    if curr[0] not in past and curr[1] not in past and depts < numfac:
      depts +=1
    past.append(curr[0])
    past.append(curr[1])


  diff = set(all) - set(past)
  depts += len(diff)

  print(depts)
