import random
import sys
from time import sleep, time


n = random.randint(1, 1000)
print(n)

guess_count = 0

guess_limit = 9      #actual try count will be 10

round_limit = 0     #actual limit will be 20

score = 0


restart = input("Want to start? Y/N ")
if restart == "N":
    print("See you next time.")
    sys.exit()


while guess_count <= guess_limit:
    if round_limit == 20:
        print("You have played the maximum number of rounds your score is:", score)
        sleep(2)
        sys.exit()
    
    guess = int(input("Enter an integer from 1 to 1000: "))
    
    guess_count += 1 
    

    if (n - guess) <= 20 and (n - guess) >= -20 and (n - guess) != 0:
        print("Your very hot")
    elif (n - guess) <= 50 and (n - guess) >= -50 and (n - guess) != 0:
        print("Your hot")
    elif guess > n and (guess) != 0:
        print("Lower")
    elif guess < n and (guess) != 0:
        print("Higher")    
    
    if guess == n:
        print("you guessed it in", guess_count,"Guesses")
        score += 1
        round_limit += 1
        guess_count = 0
        print("Your score is", score)
        n = random.randint(1, 1000)
        print(n)
        restart = input("Want to play another? Y/N ")
    if restart == "N":
        print("Your final score is", score)
        sleep(2)
        sys.exit()
    else: 
        restart == "Y"
        

    if guess_count == 10:
        print ("Sorry, the correct number is", n)
        print("Your score is", score)
        restart = input("Want to play another? Y/N ")
        if restart == "N":
            print("Your final score is", score)
            sleep(2)
            sys.exit()
        if restart == "Y":
            guess_count = 0
            round_limit += 1
            n = random.randint(1, 1000)
            print(n)