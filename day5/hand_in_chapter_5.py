#Mehmet Kino
#Hand in chapter 5 program practice
#This program will allow a user to enter bowling
#scores for a series and determine series stats for that bowler.

def display_header():
    print("Spare Time Bowling - Series Stats\n")
    
def get_series(game1, game2, game3):
    series = game1 + game2 + game3
    return series

def get_average(game1,game2,game3):
    average = (game1 + game2 + game3) / 3
    return average
    
def get_handicap(avg):
    handicap = (200 - avg) * 0.8
    return handicap

def get_league():
    league = input ("Enter Bowler's League (day or night)? ").strip().lower()
    if league == "day":
        return True
    else:
        return False

def main():
    display_header()
    
    top_day_name = ""
    top_day_avg = 0.0
    top_night_name = ""
    top_night_avg = 0.0
    
    keep_going = "Y"
    
    while keep_going =="Y".upper():
        name = input("Enter Bowler's Name: ")
        game1 = float(input("Enter Game Score 1: "))
        game2 = float(input("Enter Game Score 2: "))
        game3 = float(input("Enter Game Score 3: "))
        
        series = get_series(game1,game2,game3)
        average = get_average(game1,game2,game3)
        handicap = get_handicap(average)
        
        print(f"\nBowling Stats for {name}")
        print(f"Series {series:.0f}")
        print(f"Average {average:.3f}")
        print(f"Handicap {handicap:.3f}\n")
        
        if get_league():
            if average > top_day_avg:
                top_day_avg = average
                top_day_name = name
        else:
            if average > top_night_avg:
                top_night_avg = average
                top_night_name = name
         
        print()
        keep_going= input("Enter another Bowler? Press 'Y' to continue 'N' to stop: ").upper()
        print()
     
    display_header()
    print("TOP BOWLERS\n")
    print(f"Day League: {top_day_name} Average {top_day_avg:.3f}")
    print(f"Night League: {top_night_name} Average {top_night_avg:.3f}")
                
                
    
main()    
