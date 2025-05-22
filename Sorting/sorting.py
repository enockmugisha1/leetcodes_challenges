def reverse(x):

  y= str(x)
  z= sorted(y, reverse = True)
  print("sorted", z)
  print("".join(z))

reverse(452)
