import random # Import random for all
# Solution 1

def genEven():
    return random.randrange(0, 100, 2)

# Sol 2

def genEven():
    return random.choice(range(0, 100, 2))

# Sol 3

def genEven():
    return int(random.random() * 50) * 2
    
# Sol 4

def genEven():
    x = random.randint(0, 98)
    if (x % 2 == 0):
        return x
    else:
        return x-1
