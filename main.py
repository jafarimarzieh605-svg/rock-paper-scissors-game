import random

USER_CHOICE =("rock", "paper", "scissors")

#user
def get_user_input():
    choice = input("pick your choice [rock, paper, scissors] :")
    while choice not in USER_CHOICE :
       choice = input("pick your choice [rock, paper, scissors] :")
    return choice

#pc
def get_pc_input():
   pc_choice = random.choice(USER_CHOICE)
   print(f"pc choice was: {pc_choice}")
   return pc_choice

def determine_winner(user_input, pc_input):
 if user_input == pc_input:
    return "Draw !"
 
 elif  (user_input == "rock" and pc_input == "scissors") \
    or ( user_input == "scisors" and pc_input == "paper") \
    or ( user_input == "paper" and pc_input == "rock"):
     print("user won")

 else:
    print("Computer Won")  

def main():
    user_input = get_user_input()
    pc_input = get_pc_input()

    determine_winner(user_input, pc_input)
    print("end of program")


answer = "y"
while answer == "y":
   main()
   answer = input("Do you want to play again? yes / no ?")