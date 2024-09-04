import random as rd

print("Guessing the number")

print("Range of numbers")

start = int(input("Enter the starting point :"))
end = int(input("Enter the ending point :"))
think = rd.randint(start, end)

# Using a while loop
while True:
    guess = int(input("Guess the number :"))
    if guess > think:
        print("Guess a lower number")
    elif guess < think:
        print("Guess a higher number")
    else:
        print("You guess the correct number")
        break
