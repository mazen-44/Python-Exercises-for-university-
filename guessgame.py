import random 
num = random.randint(0,100)
attempts =0
print(num)
while True:
    try:
        number= int(input("Enter your guess (1 -> 100): "))
    except ValueError:
        print("Please Enter a valid number")
        continue    
    attempts +=1
    if number < num:
        print("Wrong guessing ,Guess a bigger one")
    elif number > num:
        print("Wrong guessing ,Guess a smaller one")
    else:
        print("Conguratulation you guessed it right")
        break
print(f"Your attempts to guess the number is {attempts}")