import random

def determine_winner(user_move, computer_move):
    winning_conditions = {
        ("rock", "scissors"): "user",
        ("scissors", "paper"): "user",
        ("paper", "rock"): "user",
        ("rock", "paper"): "computer",
        ("paper", "scissors"): "computer",
        ("scissors", "rock"): "computer"
    }

    print("user_move:", user_move)
    print("computer_move:", computer_move)

    if user_move == computer_move:
        print("It's a tie")
    elif (user_move, computer_move) in winning_conditions:
        print(f"{winning_conditions[(user_move, computer_move)]} wins!")

print("WELCOME")
print("Instructions\nThe player chooses between rock, paper, and scissors.\nThe system also randomly chooses " 
          "between rock, paper, and scissors.\nThe winner is determined by the choices.\n"
          "Rock beats scissors, Paper beats rock, and Scissors beats paper.")

user_move = input("Make a move: rock, paper, or scissors: ")
computer_move = random.choice(["rock", "paper", "scissors"])

determine_winner(user_move, computer_move)



