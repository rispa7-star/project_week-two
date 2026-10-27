import random

Player_Name = input("Enter your Player Name: ")

print(f"Welcome to Number Ninja, {Player_Name}!")

levels = input(f"{Player_Name}, choose your level: \n"
               "Easy = 10 guesses\n" 
               "Medium = 7 guesses\n" 
               "Hard = 5 guesses\n"
               "Enter your Level: ").strip().lower()

if levels == "easy":
     guesses_left = 10

elif levels == "medium":
    guesses_left = 7

elif levels == "hard":
     guesses_left = 5    

else:
     print("Invalid level!, please restart and choose Easy, Medium or Hard")
     guesses_left = 0

if guesses_left > 0:

    lucky_number = random.randint(1, 100)

    print("I am thinking of a number between 1 and 100.")

while guesses_left > 0:
  try:
        guess = int(input(f"\n {Player_Name}, Enter your lucky number: "))          
  except ValueError:
        print("Invalid Input!, please add a number.")
        continue
  if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

  if guess == lucky_number:
     print(f"Congratulations {Player_Name}!, you guessed the correct number")
     break
  elif guess > lucky_number:
            print("Oops! Your number is too high.")
  else:
            print("Oops! Your number is too low.")

  guesses_left -= 1

if guesses_left > 0:
            print(f"You have {guesses_left} guesses remaining.")
if guesses_left == 0:
        print(f"Game over! The number was {lucky_number}.")   