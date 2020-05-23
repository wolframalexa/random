if __name__ == '__main__':
  temp = map(int, input().split())
  b = temp[0]
  g = temp[1]
  num = 0

  if b < 2 or g < 2:
    print(1)

  else:
    choose = fact(b+g+2)/(fact(b)fact(2))
    num = choose/(b+g)


  print()

def factorial(n):
  if n < 2:
    return 1
  else:
    return n * factorial(n-1)
