    
def show_sum(num_1,num_2):
    result= num_1 + num_2
    print(f"The result is: {result}")

def main():
    
    num_1 = int(input("Enter first number? "))
    num_2 = int(input("Enter second number? "))
    print(f"\nThe sum of {num_1} and {num_2} is: ")
    
    show_sum(num_1, num_2)
        
main()

