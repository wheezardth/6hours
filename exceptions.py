# that's error handling
# try keyword "attempts" to run code
# except anticipates exception of some type and allows for handling
# you can have more than one exception handler per

try:
    age = int(input("Age: "))  # this will crash if you input letters
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("That's ridiculous!")
except ZeroDivisionError:
    print("Age cannot be 0.")