AllowedChar = '1234567890+-*/'
numbers = '1234567890'
sembols = '+-*/'

while True:
    operation = input("Please enter the operation to be performed:")
    
    if all(char not in numbers for char in operation):
        if all(char not in sembols for char in operation):
            print("I cannot perform this operation without any numbers or symbols entered. Please try again.")
        else:
            print("I need numbers to perform any operation. Please try again.")
    else:
        if all(char not in sembols for char in operation):
            print("I can only perform addition, subtraction, multiplication, and division. Please try again.")
        elif not all(char in AllowedChar for char  in operation):
            print("Invalid characters used. Only use +, -, *, / and numbers.")
        else:
            print("işlem yapılabilir") # Buraya işlem kod satırları eklenecek.
            break