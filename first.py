def count_number(n1, n2, n3):
  res= set([n1, n2, n3])
  if len(res)==3:
    return 0
  else:
    return (4 - len(res))

print(count_number(1, 1, 1))
print(count_number(1, 2, 2))
print(count_number(-1, -2, -3))
print(count_number(-1, -1, -1))