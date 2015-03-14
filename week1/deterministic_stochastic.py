import random

def deterministicNumber():
  return 10

#Sol 1

def stochasticNumber():
  return 2 * random.randint(5, 10)
  
# Sol2  

def stochasticNumber():
  return random.randrange(10, 22, 2)

#Sol 3

def stochasticNumber():
  x = random.randint(10, 20)
  if (x % 2 == 0):
    return x
  else:
    return x-1
