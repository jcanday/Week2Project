#Game intro and player name:
import random

"""  
  The game continues until the challenger loses. The challenger gets to choose whether he wants to continue the game if he loses. If the challenger chooses to continue, he has the opportunity to change his challenger name. The game score resets when the challenger changes his name.

"""

enter_game = input("Type Enter, Rules, or Run Away: \\n")

if enter_game.lower() == "enter":

  print("Welcome to the World of Rock, Paper, Scissors!\n\n")
  user_name = input("Enter Challenger Name:\n\n")
  
  print(f"\n\n{user_name} enters the battle!")
  
  user_score = 0
  computer_score = 0
  
  #The initiated game & options:
  while True:
  
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
  
    user_action = input("\n\nChoose your weapon: 🪨 rock, 📄paper, ✂️ scissors? \n\n")
    
    if user_action.lower() == computer_action:
        print(f"\n\nBoth players selected {user_action}. It's a tie!\n\n")
  
        #display score
        print(f"{user_name} : {user_score}    Computer : {computer_score}")
    
    elif user_action == "rock":
        if computer_action.lower() == "scissors":
            print("\n\nRock smashes scissors! You win!\n\n")
            user_score += 1
            print(f"{user_name} : {user_score}    Computer : {computer_score}\n\n")
        else:
            print("\n\nPaper covers rock! You lose.\n\n")
            computer_score +=1
  
            #display score and ask to quit
            print(f"{user_name} : {user_score}    Computer : {computer_score}\n\n")
            exit_action = input("Continue? Y/N \n\n" )
            if exit_action.lower() == "n":
              break
  
              
            else:
  
              ## Challenger chooses to change name here
              name_option = input("Change Challenger Name? Y/N \n\n")
              if name_option.lower() == "y":
                user_name = input("Enter Challenger Name:\n\n")
                computer_score = 0
                user_score = 0
    
    elif user_action.lower() == "paper":
        if computer_action == "rock":
            print("\n\nPaper covers rock! You win!\n\n")
            user_score += 1
            print(f"{user_name} : {user_score}    Computer : {computer_score}\n\n")
        else:
            print("\n\nScissors cuts paper! You lose.\n\n")
            computer_score +=1
  
            #display score and ask to quit
            print(f"{user_name} : {user_score}    Computer : {computer_score}\n\n")
            exit_action = input("Continue? Y/N " )
            if exit_action.lower() == "n":
              break
            
            else:
  
              ## Challenger chooses to change name here
              name_option = input("Change Challenger Name? Y/N \n\n")
              if name_option.lower() == "y":
                user_name = input("Enter Challenger Name:\n\n")
                computer_score = 0
                user_score = 0
              
    elif user_action.lower() == "scissors":
        if computer_action == "paper":
            print("\n\nScissors cuts paper! You win!\n\n")
            user_score += 1
            print(f"{user_name} : {user_score}    Computer : {computer_score}\n\n")
        else:
            print("\n\nRock smashes scissors! You lose.\n\n")
            computer_score +=1
  
            #display score and ask to quit
            print(f"{user_name} : {user_score}    Computer : {computer_score}\n\n")
            exit_action = input("Continue? Y/N \n\n")
            if exit_action.lower() == "n":
              break
            else:
              ## Challenger chooses to change name here
              name_option = input("Change Challenger Name? Y/N \n\n")
              if name_option.lower() == "y":
                user_name = input("Enter Challenger Name:\n\n")
                computer_score = 0
                user_score = 0
elif enter_game == "rules":
  print("\\nThe game continues until the challenger loses. The challenger gets to choose whether he wants to continue the game if he loses. If the challenger chooses to continue, he has the opportunity to change his challenger name. The game score resets when the challenger changes his name.\\n")

elif enter_game == "run away":
  exit()
else:
  print("\\n Enter valid input!!! \\n")

