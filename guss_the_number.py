# To make a simple game that creates a randum number between 1 - 100 and the user has to guess the number
# to print the number of attemps it took to guss the game 
import random
number = random.randint(1, 100)
count = 0

while True:
    
    if count > 7:
        print("guess timeout.")
        break
    
    print(number)
    try :
        user_guss = int(input("Guss the number: "))
        count += 1
        if user_guss > number :
            print("Too high")
        elif user_guss < number:
            print("Too low")
        
        else :
            print("You gussed the correct number")
            print(f"You took {count} number of times to guss the right number")
            break

    except ValueError:
        print("Entered guess is string not interger.")
        print("Enter a valid interger  number")

    