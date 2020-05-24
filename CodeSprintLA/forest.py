if __name__ == '__main__':
  num = list(map(int, input().split(' ')))
  numfac = num[0]
  numpairs = num[1]

  depts = numfac - numpairs	# if n vertices and m edges, always n-m trees
  print(depts)
