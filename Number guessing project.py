import random
secret = random.randint(1, 100)
attempts = 0
print("I'm thinking of a number between 1 and 100.")
while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess == secret:
        print(f"Correct! You took {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")