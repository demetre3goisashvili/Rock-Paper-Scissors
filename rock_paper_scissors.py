from random import randint

choices = ["rock", "paper", "scissors"]

user_input = False

while user_input == False:
    computer = choices[randint(0, 2)]
    user_input = input("Please enter Rock, Paper or Scissors: ").lower()
    if user_input == computer:
        print("computer choice:", computer)
        print("Your choice:", user_input)
        print("Tie")
    elif user_input == "rock":
        if computer == "paper":
            print("computer choice:", computer)
            print("Your choice:", user_input)
            print("You Lose!")
        else:
            print("computer choice:", computer)
            print("Your choice:", user_input)
            print("You Win Congratulations!")
    elif user_input == "scissors":
        if computer == "rock":
            print("computer choice:", computer)
            print("Your choice:", user_input)
            print("You Lose!")
        else:
            print("computer choice:", computer)
            print("Your choice:", user_input)
            print("You Win Congratulations!")
    elif user_input == "paper":
        if computer == "scissors":
            print("computer choice:", computer)
            print("Your choice:", user_input)
            print("You Lose!")
        else:
            print("computer choice:", computer)
            print("Your choice:", user_input)
            print("You Win Congratulations!")
    else:
        print("Invalid input! Please enter Rock, Paper, or Scissors.")
    user_input = False
    
   

    


    
