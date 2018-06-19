import random
moves =["rock","paper","scissor"]
print("----------Welcome to the game of ROCK-PAPER-SCISSORS-----------")
total_moves = 0
your_score =0
computer_score =0
while True:
    computer_move=random.choice(moves)
    user_move = input("Enter your move:[rock,paper or scissor]:")
    if computer_move == "rock" and user_move == "scissor":
        print("Opponent move:",computer_move)
        print("Opponent scores !!!")
        total_moves=total_moves+1
        computer_score = computer_score +1
    elif computer_move == "scissor" and user_move == "paper":
        print("Opponent move:",computer_move)
        print("Opponent scores !!!")
        total_moves=total_moves+1
        computer_score = computer_score +1
    elif computer_move == "paper" and user_move == "rock":
        print("Opponent move:",computer_move)
        print("Opponent scores !!!")
        total_moves=total_moves+1
        computer_score = computer_score +1
    elif computer_move == user_move:
        print("Opponent Move",computer_move)
        print("Nobody scores !!")
        total_moves = total_moves +1
    else:
        print("Opponent move:",computer_move)
        print("You score !!!!!")
        total_moves=total_moves+1
        your_score=your_score+1
    choice=input("Continue ?? [yes/no]:")
    if choice == "no":
        break

print("---------------------------------")
print("Total moves:",total_moves)
print("Your score:",your_score)
print("Computer score:",computer_score)
if your_score > computer_score:
    print("YOU WON !!!!!!!")
elif your_score == computer_score:
    print("It's a tie !!!")
else:
    print("You Lose !!! Better Luck next time !!!")

