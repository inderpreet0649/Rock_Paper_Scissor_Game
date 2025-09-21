import random
import time

# Take player Name
def Player_name():
    Player_name = input("Hey user please enter your Name : ").strip().capitalize()
    return Player_name

#items name
items_list = ["Rock" , "Paper" , "Scissor"]

# user choice(choose marker)
def Player_choice():
    while True:
        Choice = input("enter your choice : ").strip().capitalize()
        if Choice in items_list:
            return Choice 
        else:
            print("invalid choice ! please enter Rock Paper Scissor")

#Computer choice
def Comp_choice():
    return random.choice(items_list)

#display choice (with ASCII art)
def display_choice(Player_choice ,Comp_choice):
    print("\n=== ROUND ===")
    print("Yours choice:")
    if Player_choice == "Rock":
        print("  __  ")
        print(" /  \ ")
        print(" \__/ ")
    elif Player_choice == "Paper":
        print(" ___ ") 
        print("|___|") 
    elif Player_choice == "Scissor":
        print("  //\\  ")
        print(" //  \\ ")
        print("//    \\ ")
    print(f"{Player_name} you choose = {Player_choice}")
    
    if Comp_choice == "Rock":
        print("  __  ")
        print(" /  \ ")
        print(" \__/ ")
    elif Comp_choice == "Paper":
        print(" ___ ") 
        print("|___|") 
    elif Comp_choice == "Scissor":
        print("  //\\  ")
        print(" //  \\ ")
        print("//    \\ ")
    print(f"Computer choose : {Comp_choice}")  

#Check Winner
def check_winner(Player_choice , Comp_choice):
    if Player_choice == Comp_choice:
        return "Tie"
    elif (Player_choice == "Rock" and Comp_choice == "Scissor") or (Player_choice == "Paper" and Comp_choice == "Rock") or (Player_choice == "Scissor" and Comp_choice == "Paper"):
        return "Player"
    else:
        return "Computer"

#Update Score
def update_score(Winner ,Player_score , Comp_score):
    if winner == "Player":
        Player_score += 1
    elif winner == "Computer":
        Comp_score += 1 
    return Player_score , Comp_score

#display score
def display_score(Player_name , Player_score , Comp_score):
    print(f"Score - {Player_name} : {Player_score} | Computer : {Comp_score}")
#Play Again
def play_again():
    return input("Do you want to play again?  (yes/no) :  ").strip().capitalize() == "Yes"

#End Game
def end_game(Player_name , Player_score , Comp_score):
    print(f"Final Score - {Player_name}: {Player_score} | Computer : {Comp_score}")
    if Player_score > Comp_score:
        print(f"Congratulations {Player_name} ! you are the overall winner!")
    elif Comp_score > Player_score :
        print("computer win overall")
    else:
        print("its a tie overall")

#Main game loop
Player_name = Player_name()
print(f"\nWelcome , {Player_name}! Let's start game")
Player_score = 0
Comp_score = 0
while True:
    print("Computer is choosing" , end = "")
    for _ in range(3):
        print("." , end ="", flush = True)
        time.sleep(0.5)
    

    player_choice = Player_choice()
    comp_choice = Comp_choice()
    display_choice(player_choice , comp_choice)

    winner = check_winner(player_choice , comp_choice)
    if winner == "Tie":
        print("Result:===TIE===")
    else:
        print(f"Result:{winner} wins this round!")
    Player_score , Comp_score = update_score(winner , Player_score , Comp_score)
    display_score(Player_name , Player_score , Comp_score)

    if not play_again():
        break

end_game(Player_name , Player_score , Comp_score)