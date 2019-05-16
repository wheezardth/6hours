# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = 2019

print(f"Hey, {name} you will be 100 years old in {current_year+(100-age)}")