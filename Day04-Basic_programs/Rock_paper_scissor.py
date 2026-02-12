import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
R_P_S = [rock, paper, scissors]
print("what do you choose?")
user_chose = int(input("type 0 for rock, 1 for paper, 2 for scissors: "))
if user_chose >= 0 or user_chose <= 2:
    print(R_P_S[user_chose])
computer_chose = random.randint(0,2)
print("computer chose :")
print(R_P_S[computer_chose])
if user_chose >= 3 or user_chose <= 0:
    print("u have choose invalid number")
elif user_chose == 0 and computer_chose == 2:
    print("you win")
elif computer_chose == 0 and user_chose == 2:
    print("you lose")
elif computer_chose > user_chose:
    print("you lose")
elif computer_chose < user_chose:
    print("you win")
elif computer_chose == user_chose:
    print("its a draw")
