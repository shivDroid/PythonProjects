import random,sys

sys_guess = random.randint(1,20)
print("I am thinking of a number between 1 and 20, take a guess?")

number_of_guess = 0 
while True: 
    user_guess = int(input("Enter your guess:  "))
    number_of_guess = number_of_guess + 1
    if user_guess == sys_guess:
        print(f"Wohooooo! Congratulations you guessed the number right. It took you {number_of_guess} attempts")
        sys.exit()
    elif user_guess - sys_guess == -4 or user_guess - sys_guess == 4:
        print("You are close!!!") 
    elif user_guess < sys_guess:
        print("Your guess is lower than mine")
    else:
        print("Your guess is higher than mine") 
    
         


