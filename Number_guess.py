import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
        
        except ValueError:
            print("Please enter a valid number!")
    
    else:
        print(f"Game over! The number was {secret_number}.")

# Run the game
guess_the_number()
