import random
def game():
    logo = '''
     ___                       _   _                __                 _               
    / _ \_   _  ___  ___ ___  | |_| |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
   / /_\/ | | |/ _ \/ __/ __| | __| '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
  / /_\\| |_| |  __/\__ \__ \ | |_| | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
  \____/ \__,_|\___||___/___/  \__|_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   

  '''
    print(logo)
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    flag = True
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
        print(f"You have {attempts} remaining to guess the number.")
    elif difficulty == 'hard':
        attempts = 5
        print(f"You have {attempts} remaining to guess the number.")
    while flag is True:
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            flag = False
        elif guess > answer:
            print("Too high.\nGuess again.")
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number.")
        elif guess < answer:
            print("Too low.\nGuess again.")
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number.")
        if attempts == 0:
            print("You lose. You run out of attempts.")
            return
game()
