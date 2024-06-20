import random,sys

sys_guess = random.randint(1,20)
print("I am thinking of a number between 1 and 20, take a guess?")

while True: 
    user_guess = int(input("Enter your guess:  "))
    if user_guess == sys_guess:
        sys.exit()
    elif user_guess - sys_guess == -4 or user_guess - sys_guess == 4:
        print("You are close!!!") 
    elif user_guess < sys_guess:
        print("Your guess is lower than mine")
    else:
        print("Your guess is higher than mine")  


