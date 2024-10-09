import random
number = random.randint(1,10)
attempts = 3
count = 1
while count <= attempts:
    guess = int(input("Guess the correct number between 1-10: "))
    if (guess > number): 
        print("Too high")
    elif (guess < number):
        print("Too low")
    else: 
        print("Correct")
        break

    count+=1