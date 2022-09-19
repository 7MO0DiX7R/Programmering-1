import random
computer_score = 0
user_score = 0

while computer_score < 3 and user_score < 3:
    computer = random.choice(["rock", "paper", "scissors"])

    user = input("rock, paper or scissors? ")

    print("The computer chose", computer,"and the user chose", user +".")

    if computer == "rock" and user == "scissors":
        computer_score += 1
        print("Computer got a point ") 
        print(computer_score, user_score)

    elif computer == "paper" and user == "rock":
        computer_score += 1
        print("Computer got a point") 
        print(computer_score, user_score)

    elif computer == "scissors" and user == "paper":
        computer_score += 1
        print("Computer got a point") 
        print(computer_score, user_score)

    elif computer == "rock" and user == "paper":
        user_score += 1
        print("You got a point") 
        print(computer_score, user_score)

    elif computer == "scissors" and user == "rock":
        user_score += 1
        print("You got a point") 
        print(computer_score, user_score)

    elif computer == "paper" and user == "scissors":
        user_score += 1
        print("You got a point") 
        print(computer_score, user_score)

    # TODO - Implement the if statements that prints who wins