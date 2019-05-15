# no need for type definition - type auto-resolves
# multiple arguments are separated by commas

def greet_user(name):
    print(f"Hi {name}")
    print("Welcome Aboard!")


print("Start")
greet_user("John")
greet_user("Mary")
greet_user(101101011) #will take valid integer as well

# function "overloading" is handled by using None as a default values for arguments
# and then handled as an internal if check

def happy_birthday(name=None, age=None):
    if name is not None and age is not None:
        print(f"Hi {name}, Happy {age}st Birthday!")
    elif name is not None:
        print(f"Hi {name}, Happy Birthday!")
    else:
        print("Happy Birthday!")


happy_birthday("Jamie", 21)
happy_birthday("Laura")
happy_birthday()


# 2:43:58
# keyword arguments allow to address the keywords in whatever order we want
# that's mostly for code readability

happy_birthday(age = 96, name = "Inverso")

