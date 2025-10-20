import random
#print this 5 times

str ="The message is succesfull"

for nuumber in range(0,5) :
    print(str)

print("########################")

for number in range (0,10,2): #(starting , ending, step)
    print(number)

print("##########################")    

truth_list= [True, False, True, False, False]
randomly_picked_from_list = random.choice(truth_list)
print(randomly_picked_from_list)

while randomly_picked_from_list == True:
    print("It seems like, He is telling the truth")
    randomly_picked_from_list = False
    while randomly_picked_from_list == False:
        print("But the Truth Machine says he is liying")
        randomly_picked_from_list = True
        
        
    break
if randomly_picked_from_list == False:
   print("He is liying")   

