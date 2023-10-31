import random

random_num= random.randint(1,100)
print(random_num)

random_float= random.random()
print(random_float)

random_side=random.randint(0,1)
if random_side==1:
  print("Head")
else:
  print("Tail")