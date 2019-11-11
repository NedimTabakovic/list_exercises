
still_playing = True

# print("about to run whe while loop")
while still_playing:
    try:    
        users_number = int(input("Give me a number! "))
        if users_number > 3:
            print("too high!")
        elif users_number == 3:
            print("you guessed correctly!")  
            still_playing = False  
        else: 
            print("too low")    

    except ValueError
        print("Please type a number beyotch")


        