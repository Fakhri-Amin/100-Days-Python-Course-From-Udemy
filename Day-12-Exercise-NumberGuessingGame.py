import random

random_num = random.randint(1, 100)
attempt = 0
game_end = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard' : ")

if user_choice.lower() == "easy":
    attempt = 10
elif user_choice.lower() == "hard":
    attempt = 5
else:
    print("Invalid input")

while not game_end and attempt > 0:
    print(f"You have {attempt} attempts remaining to guess the number")
    guess = int(input("Make a guess : "))
    if guess == random_num:
        game_end = True
    else:
        attempt -= 1
        if guess > random_num:
            print("Too high")
        else:
            print("Too low")

if game_end and attempt > 0:
    print(f"Well guessed, its {random_num}")
elif attempt == 0:
    print(f"You ran out of attempts. You lost. Its {random_num}")
