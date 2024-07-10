# Rock-Paper-Scissors Game
import random
random.seed() 

# Function to take input from user 
def get_user_input():
    while True:
        user_input = input("Enter your choice (rock, paper or scissors): ")
        user_input = user_input.lower()
        if user_input in ['rock','paper','scissors']:
            return user_input
        else :
            print("Invalid Input. Try Again!")

# Function for computer to randomly choose a option
def get_computer_choice():
    comp_input = ['rock','paper','scissors']
    return random.choice(comp_input)

# Function to define game's logic
def game_logic(user_choice,comp_choice):
    if (user_choice == comp_choice):
        return "It's a tie!"
    elif (user_choice == 'rock' and comp_choice == 'scissors') or (user_choice == 'scissors' and comp_choice == 'paper') or (user_choice == 'paper' and comp_choice == 'rock'):
        return "You won ! Congratulations."
    else :
        return "You lose ! Better Luck Next Time."
    
# Function to play the game and also track the score
def play_game():
    user_score = 0
    comp_score = 0
    while True:
        user_choice = get_user_input()
        comp_choice = get_computer_choice()
        print("You chose :",user_choice)
        print("Computer Chose :",comp_choice)
        result = game_logic(user_choice,comp_choice)
        print(result)
        # Score_tracking
        if result == "You won ! Congratulations.":
            user_score += 1
        elif result == "You lose ! Better Luck Next Time.":
            comp_score += 1
        print("Your score :",user_score)
        print("Computer Score :",comp_score)
        # Whether to continue or exit
        play_again = input("Do you want to play again?(yes/no) :")
        if play_again.lower() == 'no':
            break

print("WELCOME TO ROCK-PAPER-SCISSORS GAME !")
play_game()