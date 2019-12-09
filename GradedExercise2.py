#Russell Halenda
#November 14th, 2019
#Program that when ran, prompts the user to input
#   a basic function of calculator, and then
#   perform it with user-input numbers.
import sys
print(sys.executable)
print(sys.version)


while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
      num1 = float(input("Enter the 1st number: "))
      num2 = float(input("Enter the 2nd number: "))
      result = str(num1 + num2)
      print("The result is: " + result + "\n")
   elif user_input == "subtract":
      num1 = float(input("Enter the 1st number: "))
      num2 = float(input("Enter the 2nd number: "))
      result = str(num1 - num2)
      print("The result is: " + result + "\n")
   elif user_input == "multiply":
      num1 = float(input("Enter the 1st number: "))
      num2 = float(input("Enter the 2nd number: "))
      result = str(num1 * num2)
      print("The result is: " + result + "\n")
   elif user_input == "divide":
      num1 = float(input("Enter the 1st number: "))
      num2 = float(input("Enter the 2nd number: "))
      result_whole = str(num1 // num2)
      result_int = str(num1 / num2)
      rem = str(num1 % num2)
      print("The result is: " + result_whole + " with remaider of " + rem + "\nOR: " + result_int + "\n")
   else:
      print("Unknown input")
