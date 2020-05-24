import math

if __name__ == '__main__':
  temp = map(int, input().split())
  b = temp[0]
  g = temp[1]
  N = b+g
  num = 0

  if b < 2 or g < 2:
    num = 1

  else:
    num = (math.comb(N,b)+N*math.comb(math.floor(N/2),math.floor(b/2)))/(2*N)
    # divide out reflections and rotations
  print(num)
