#Mehmet Kino
#Hand in Chapter 7 program practice
#This is updated version of program from chapter 5 and The program should still allow a user to enter player information and calculate
#statistics for that player.

import validator

def display_header():
    print("Spare Time Bowling - Series Stats\n")

def enter_series(scores):
    for i in range(len(scores)):
        prompt = f"score {i+1}"
        scores[i] = validator.is_within_rangeI(0, 300, prompt)

def get_series(scores):
    series = 0
    for g in scores:
        series += g
    return series

def get_average(scores):
    series_total = get_series(scores)
    average = series_total / len(scores)
    return average

def display_averages(averages, bowlers):
    print("\nBowlers Averages")

    total_avg = 0
    for i in range(len(bowlers)):
        print(f"{bowlers[i]:<10} {averages[i]:.3f}")
        total_avg += averages[i]

    overall_avg = total_avg / len(averages)
    print(f"Overall Average: {overall_avg:.3f}")


def main():
    display_header()

    bowlers = []      
    averages = []     

    keep_going = "Y"

    while keep_going.upper() == "Y":
        name = validator.required_entry("Enter Bowler's Name: ")
        bowlers.append(name)

        scores = [0] * 5

        enter_series(scores)

        
        avg = get_average(scores)
        averages.append(avg)

        print(f"\n{name}'s Series Total: {get_series(scores)}")
        print(f"{name}'s Average: {avg:.3f}\n")

        keep_going = input("Enter another bowler? (Y/N): ")
        print()

    
    display_averages(averages, bowlers)


main()