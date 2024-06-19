import random as rd

while True:
    players = ["BRAINER", "WESLEY", "PSALMIST", "BEN"]
    print(" WELCOME TO THE OFLINE GUESS GAME")
    print(" ")
    print("=====================================================================================")
    print(" ")
    print("Enter Your Name Below OR Type 'NO' to Exit Game!")
    name = input("What Is Your Name?:")
    print(" ")
    
    print("=====================================================================================")
    print("Hi {}, I am Thinking Of A Number Between 1 and 50".format(name))
    print(" ")
    print("Please Help {} guess the Number Correctly!".format(rd.choice(players)))
    print(" ")
    print("Else Type: A String to end game!")

    print("=====================================================================================")
    print(" ")
    guessed = rd.randint(0,50)
    num_of_guess = []
    
    if name.lower() == "no":
        print("GOODBYE FROM GUESS GAME!")
        break


    while guessed:
        guess_user = int(input("guess the number: "))
        #num_of_guess.append(guess_user)
        if guess_user > guessed:
            if guess_user - guessed > 10:
                print("Your Guess Is Too FAR GREATER Than My Actual Number") 
            else:
                print("Your Guess Is Near My Actual Number But GREATER Than It")
            num_of_guess.append(guess_user)
        elif guess_user < guessed:
            if guessed - guess_user > 10:
                print("Your Guess Is Too FAR LOWER Than My Actual Number")
            else:
                print("Your Guess Is Near My Actual Number, But LESS Than It")
            num_of_guess.append(guess_user)
            
        else:
            if len(num_of_guess) == 1:
                print("============================================================================")
                print("YOU ARE A GENIUS!!")
                print("{} guessed: {} Correctly in {} Guess".format(name, guessed, len(num_of_guess)))
                print("============================================================================")
                print(" ")
            elif len(num_of_guess)<=5 and len(num_of_guess)>1:
                print("============================================================================")
                print("EXCELLENT GUESS!")
                print("{} guessed: {} Correctly in {} Guesses".format(name, guessed, len(num_of_guess)))
                print("============================================================================")
                print(" ")
            elif len(num_of_guess)<=15 and len(num_of_guess)>5:
                print("============================================================================")
                print("Good GUESS!")
                print("{} guessed: {} Correctly in {} Guesses".format(name, guessed, len(num_of_guess)))
                print("============================================================================")
                print(" ")
            elif len(num_of_guess)<=25 and len(num_of_guess)>15:
                print("============================================================================")
                print("Fair GUESS!")
                print("{} guessed: {} Correctly in {} Guesses".format(name, guessed, len(num_of_guess)))
                print("============================================================================")
                print(" ")
            elif len(num_of_guess)<=50 and len(num_of_guess)>25:
                print("============================================================================")
                print("Very Poor GUESS!, Please Try And Think Faster To Guess Better...")
                print("{} guessed: {} Correctly in {} Guesses".format(name, guessed, len(num_of_guess)))
                print("============================================================================")
                print(" ")
            break
        #if guess_user == 100:
            #break
