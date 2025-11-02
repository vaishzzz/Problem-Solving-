import random

User_choice = input("Choose : Rock, Paper, Scissor \n") 
print("You have selected:", User_choice)
if User_choice =="Rock":
    User_choice = 1
elif User_choice == "Paper":
    User_choice = 2
elif User_choice =="Scissor":
    User_choice = 3
else: print("Enter valid option")

number= random.randint(1,3)

if number == 1:
    print("Rock")
elif number == 2:
    print("Paper")
else: print("Scissor")


if User_choice == number:
    print("Yeppy!! you won")
else: 
    print("Better luck next time")