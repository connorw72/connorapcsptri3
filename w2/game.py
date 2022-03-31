import random
def play():
  pick = ["Rock", "Paper", "Scissors"]

  enemy = random.choice(pick)
  you = False

  while you == False:
    you = input("What do you pick? Rock, Paper, or Scissors?")
    if you == enemy:
        print("You tied the enemy")
    elif you == "Rock":
        if enemy == "Paper":
            print("The enemies", enemy, "beat your", you, "! You lose!")
        else:
            print("Your", you, "beat the enemies", enemy, "! You win!")
    elif you == "Paper":
        if enemy == "Scissors":
            print("The enemies", enemy, "beat", you, "! You lose!")
        else:
            print("Your", you, "beat the enemies", enemy, "! You win!")
    elif you == "Scissors":
        if enemy == "Rock":
            print("The enemies", enemy, "beat", you, " ! You lose!")
        else:
            print("Your", you, "beat the enemies", enemy, "! You win!")
    else:
        print("Nope! This is case sensitive!")

