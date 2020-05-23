if __name__ == '__main__':
  list_temp = list(map(int, input().split()))
  n = list_temp[0]
  k = list_temp[1]
  d = list_temp[2]
  themes = map(int, input().split())
  schedules = 0


  nums = [bin(i) for i in range(2**5)]
  print(nums)
  dbin = bin(d)

  for i in nums:
    for j in nums:
      xored = int(i,2)^int(j,2)
      xored = str(bin(xored))
      onespos = [i+1 for i in range(len(xored)) if xored[i] == '1']
      if onespos == themes and i+j == dbin:
        schedules += 1

  print(schedules)
