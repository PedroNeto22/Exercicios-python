def create_multiply(num_multi):
  def multiplied(num):
    return num_multi * num
  return multiplied

quadruplicar = create_multiply(4)
triplicar = create_multiply(3)
duplicar = create_multiply(2)

print(quadruplicar(4))
print(triplicar(4))
print(duplicar(4))