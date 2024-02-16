name = input("Enter your name:")
while True:
    if any(char.isdigit() for char in name):
        print("Your name cannot contain numbers.")
    else:
        try:
            age = int(input("Enter your age:"))
        except ValueError:
            print("Please make sure to enter your age as a numerical value.")
        else:
            name = name.title()
            final = "Your name is {} and your age is {}."
            print(final.format(name,age))
            break