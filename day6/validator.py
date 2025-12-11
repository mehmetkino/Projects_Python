#This module contains Validation Functions
# these are generic validation and can be used with any program


def main():
    print('Hello from Validator')
    
    
def get_integer(message):
    value = 'ERR'
    
    while value == 'ERR':
        try:    
            value = int(input("Enter " + message + " "))
            
        except ValueError:
            print("ERROR:", message, "Must be an integer value")
            
    return value 
        
    
def get_float(message):
    value = 'ERR'
    
    while value == 'ERR':
        try:    
            value = float(input("Enter " + message + " "))
            
        except ValueError:
            print("ERROR:", message, "Must be a decimal value")
            
    return value 
        
def is_within_rangeF(min, max, message):
     
    value =  get_float(message) 
     
    while value < min or value > max:
     
        value = get_float(f'{message} must be within range of {min} to {max} ')
    
    return value

def is_within_rangeI(min, max, message):
    
    value =  get_integer(message) 
            
    while value < min or value > max:
         
        value = get_integer(f'{message} must be within range of {min} to {max} ')
    
    return value

def required_entry(message):
    value =  input("Enter " + message + " ")
    while value == "":
        value = input(message + "  - Please re-enter ")
    
    return value

def is_numeric(message):
     value =  input("Enter " + message + " ")
     while not(value.isnumeric()):
         value = input("Error " + message + " must be a numeric entry, Please re-enter ")
     
     return value
    
def getLetterGrade(message):
    lettergrd = ("A+", "A", "B+", "B", "C+", "C", "D+", "D", "F")
    value = requiredEntry(message).upper()
    
    while not(value in lettergrd):
        value = input("Error " + message + " must be a valid grade from the SCC Grade Scale ").upper()
            
    return value
        
def isValidEmail(message):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    value = input(f'Enter {message} ')
    
    while not(re.fullmatch(regex, value)):
        print("InValid Email")
        value = input(f'Enter {message} ')
    return value

def isValidPhone(message):
    regex = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
    
    value = input(f'Enter {message} ')
    
    while not(re.fullmatch(regex, value)):
        #print("InValid Email")
        value = input(f'Enter {message} ')
    return value

 