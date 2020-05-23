if __name__ == '__main__':
  num = int(input())
  bnum = bin(num)
  bnum = map(int, list(str(bnum)[2:]))
  print(sum(bnum))
