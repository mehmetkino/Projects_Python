veggies = ["lettuce", "onions","potatos"]
fruits = ["apple", "orange","pear","watermelon"]

dirty_fuits =[veggies, fruits]

print(dirty_fuits)# This will print 2 seperate lists. It is nested lists
print("######################")

#The len() function returns the number of items in an object.

number_of_items_in_veggies = len(veggies)
number_of_items_in_fruits = len(fruits)

print(number_of_items_in_fruits) #length and index are 2 different things be carefuk with range.
print(number_of_items_in_veggies)
print(fruits[-3]) #counts from the end of list to first item starting at 1

print("########################")
print(dirty_fuits[0][1])