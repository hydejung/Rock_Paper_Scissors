import random
import time

# Game Images
rock = '''      _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ '''

paper = ''' _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              '''

scissors = '''          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ 
|___/\___|_|___/___/\___/|_|  |___/'''

game_images = [rock,paper,scissors]

should_end = True

while should_end:
      user_choice = int(input("What do you want to choose ?\nType 0 for Rock,\nType 1 for Paper\nor Type 2 for Scissors\n :"))
      print("\nYou Choose : ")
      if user_choice >= 3 or user_choice < 0:
            print("You choose invalid number, YOU LOSE !!!")
            play_again = input("\nDo you want to play again ? Type 'y' for Yes or Type 'n' for No").lower()
            if play_again == 'y':
                  should_end = True
            else:
                  should_end = False
                  print("End Program")
      else:
            print(game_images[user_choice])
            
            computor_choice = random.randint(0,2)
            print("\nComputer Choose :\n")
            print(game_images[computor_choice])
            
            if user_choice == 0 and computor_choice == 2:
                  print("\nYou WIN !!!")
            elif computor_choice == 0 and user_choice == 2:
                  print("\nYou LOSE !!!")
            elif computor_choice > user_choice:
                  print("\nYou LOSE !!!")
            elif user_choice > computor_choice:
                  print("\nYou WIN !!!")
            elif user_choice == computor_choice:
                  print("\nIt's a DRAW !!!")
            
            new_game = input("Do you want to play again ? Type 'y' for Yes or Type 'n' for No").lower()
            if new_game == 'y':
                  should_end = True
            else:
                  should_end = False
                  print("END GAME")
            
      
