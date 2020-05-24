if __name__ == '__main__':
  list_temp = list(map(int, input().split()))
  n = list_temp[0]
  k = list_temp[1]
  d = list_temp[2]
  themes = map(int, input().split())

  if d > 2**(n+1):
    schedules = 0

  else:
    for i in themes: # remove theme night earnings from sum
      d -= 2**(i)

    if d < 0 or d % 2 == 1:
      schedules = 0

    else:
      schedules = 2**k

  print(schedules)
