import random
a = int(input("Enter the lower limit of the number: "))
b = int(input("Enter the upper limit of the number: "))
secret_number = random. randint(a, b)
print("I have chosen a number between", a, "and", b, ". Try to guess it.")
running = True
while running:
    number = int(input("Enter a guess: "))
    if number < secret_number:
        print("Your guess is TOO LOW...")
        print("Try again")
    elif number > secret_number:
        print("Your guess is TOO HIGH.. ")
        print("Try again")
    elif number == secret_number:
        print("Congrats! The number was: ", secret_number)
        break
