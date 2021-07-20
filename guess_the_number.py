import random

easy = 10
hard = 5
is_on = True

print("Welcome to Number guessing game!\n")
print("I'm thinking a number between 1 to 100.\n")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


while is_on:
  if difficulty == 'easy':
    print(f"You have {easy} attempts remaining to guess the number ")
    guess = int(input("Make a guess: "))
    if guess > number:
      print("To high")
    elif guess < number:
      print("To low")
    elif guess == number:
      print(f"You've guessed right! The number is: {number}")
      print("Congratulations! You win.")
      is_on = False
    easy -= 1
    if easy == 0 and guess != number:
      print("You've run out of guesses, you lose.")
      is_on = False

  elif difficulty == 'hard':
    print(f"You have {hard} attempts remaining to guess the number ")
    guess = int(input("Make a guess: "))
    if guess > number:
      print("To high")
    elif guess < number:
      print("To low")
    elif guess == number:
      print(f"You've guessed right! The number is: {number}")
      print("Congratulations! You win.")
      is_on = False
    hard -= 1
    if hard == 0 and guess != number:
      print("You've run out of guesses, you lose.")
      is_on = False