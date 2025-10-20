#This program will randomly pick a name from list
print("Below is option 1")
import random
#in order to use random we need to import it!

friends= [ "Alice", "Bob","Charlie","David","Emanuel"]
picked_name =random.choice(friends)
print(picked_name)



#use randint(value, value)
print("This is option 2")
random_index = random.randint(0,4) 
# this is index from 0 to 5. it is our list
#It will randomly choice an index number whenever we run it.

print(friends[random_index])