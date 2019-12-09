#Russell Halenda
#December 1st, 2019
#Program that asks the user to input two integers, and then how they'd like to transform them using the functions provided.
#Program takes advantage of the import function, and functions defined in the math library.
#Program also takes advantage of formatted string literals and the f / format methof of strings

while True:
    import math

    def add(x,y): #defines the addition function to add two numbers together.
        result = x+y
        return result

    num1 = input("Enter the first number, or 'quit' to quit: ")
    if num1 == "quit":
        break
    else:
        num1 = float(num1)

    num2 = float(input("Enter the second number: "))

    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'power' to exponentiate a number")
    print("Enter 'gcd' to find the greatest common denominator of two numbers")
    print("Enter 'hypot' to find the hypotenue of two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
       break

    elif user_input == "add":
        result = str(num1 + num2)
        print (F"The result is {result}")

    elif user_input == "subtract":
        result = str(num1 - num2)
        print (F"The result is {result}")

    elif user_input == "multiply":
        result = str(num1 * num2)
        print (F"The result is {result}")

    elif user_input == "divide":
       if num1 or num2 == "0":
            print("Cannot divide by 0. \n")
            continue
        else:
            result_whole = str(num1 // num2)
            result_int = str(num1 / num2)
            rem = str(num1 % num2)
            print(F"The result is {result_whole} with a remainder of {rem} OR {result_int}")

    elif user_input == "power":
        result = str(num1**num2)
        print(F"The result of {num1} to the {num2} power is {result}")

    elif user_input == "gcd":
        num1 = int(num1)
        num2 = int(num2)
        result = math.gcd(num1, num2) #Called the gcd function from the math library to find the greatest common denominator
        print(F"The greatest common denominator of {num1} and {num2} is {result}")

    elif user_input == "hypot":
        result = str(math.hypot(num1, num2)) #Called the hypot function from the math library to find the hypotenuse
        print(F"The hypotenuse of {num1} and {num2} is {result}")

    else:
        print("Unknown input")

    print("\n")
