import random

print("Welcome to Rock-Paper_Scissor!\n")
print("Winning Rules: ")
print("Rock VS Paper Wins -> Paper Wins")
print("Rock VS Scissors -> Rock Wins")
print("Paper VS Scissors -> Scissors Wins")
choices=["Rock","Paper","Scissors"]
while True:
    print("Choose an option: ")
    print("1-Rock")
    print("2-Paper")
    print("3-Scissors")

    try:
       choice=int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue
    while choice<1 or choice>3:
        choice = int(input("Please enter a valid choice (1-3): "))
    user_choice=choices[choice-1]
    print("/n User choice is :",user_choice)
    print("Now,Computer's turn....")
    comp_choice=random.randint(1,3)
    computer_choice=choices[comp_choice-1]
    print("Computer choice is: ",computer_choice)
    print(user_choice,"VS",comp_choice)
    if choice==comp_choice:
        print("-----It's a Tie!----")
    elif(
        (choice==1 and comp_choice==3)or
        (choice==2 and comp_choice==1)or
        (choice==3 and comp_choice==2)
    ):
        print("-----User Wins!-----")
    else:
        print("-----Computer wins!----")
    while True:
        ans=input("\n Do you want to play again?(Y/N): ").lower()
        if ans in ['y','n']:
            break
        print("Please enter Y or N.")
    if ans=='n':
        break
    print()
print("\n Thanks for playing!")