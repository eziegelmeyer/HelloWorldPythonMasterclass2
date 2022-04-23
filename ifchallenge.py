name = input("What is your name? ")
age = int(input("How old are you, {0}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to the holiday, {0}!".format(name))
else:
    print("Sorry, but you don't qualify.")