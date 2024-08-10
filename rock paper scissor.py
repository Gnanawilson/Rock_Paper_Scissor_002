#rules: rock win against scissor
#       scissor win against paper
#       paper win against rock   
#     user choise       computer choise result
#     |  0                  0          ->draw
#rock |  0                  1          ->comp-win
#     |__0__________________2          ->user-win
#     |  1                  0          ->user-win
#paper|  1                  1          ->draw
#     |__1__________________2          ->comp-win
#     |  2                  0          ->comp-win
#sciss|  2                  1          ->user-win
#     |__2__________________2          ->draw
# if com>user
#    ->you win
#if user>com
#     ->you loss
#if user==0 and com==2
#     ->you win
#if user==2 and com==0
#     ->you loss
import random
rock= '''
   _______,
---    ____)
      (_____)
      (_____)
      (____)
---._(___)
         
'''
paper = ''' 
   ________
---    ____)__
        ______)_
         ______)
       _______)
---.________)
'''
scissors = ''' 
   ________
---     ___)____
        ________)
         _______)
    (______)
---._____)
'''

game_images= [rock,paper,scissors]
user_choise=input("Enter your Choise: type 0 for rock,type 1 for papper,type 2 for scissor:(0/1/2):")

if int(user_choise)>=3 or int(user_choise)<0:
    print(" You entered Invalid number,you also loss ")
else:
    print("user choise:",game_images[int(user_choise)])
    #print(game_images[int(user_choise)])
    computer_choise=random.randint(0,2)
    print("Computer_choise 💻:",game_images[int(computer_choise)])
    #print(game_images[int(computer_choise)])
    #print(f"Computer choise💻:{computer_choise}")
    if computer_choise==int(user_choise):
        print("It is draw")
    elif computer_choise>int(user_choise):
        print("you lose👎")
    elif computer_choise<int(user_choise):
        print("You win🏆")
    elif int(user_choise)==0 and computer_choise==2: 
        print("You lose👎")
    elif int(user_choise)==2 and computer_choise==0: 
        print("You win🏆")