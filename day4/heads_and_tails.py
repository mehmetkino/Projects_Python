#Create a coin flip program. It should print 
#"head" or "tails" everytime it runs

import random

random_number = random.randint(0,1)
print(random_number)
if random_number == 0:
    print("Heads")
else:
    print("Tails")
