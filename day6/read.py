file_path ="C:/Users/mehme/OneDrive/Desktop/input.txt"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found!")  
except PermissionError:
    print("The permission is denied!")      
print("##########")

#to append a new line

try:
    with open(file_path,'a') as formatted_file:
        formatted_file.write("One more time I do not like pizza")
        print("The sentence was added succesfully")
        print("After adding a new string", formatted_file)
except PermissionError:
    print("You do not have permission!") 
except FileNotFoundError:
    print("That file was not found!")            