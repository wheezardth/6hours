# dictionary is kind of like a class
#curly braces make a dictionary
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer) #print function can do that too

print(customer["name"]) #square brackets for addressing
# print(customer["Name"]) #case sensitive, will give error

print(customer.get("birthdate"))                # doesn't cause error, returns None
print(customer.get("birthdate", "Jan 1 1980"))  # instead of None, returns second argument

customer["name"] = "Jack Daniel" #square brackets for assigning
print(customer["name"])
customer["birthdate"] = "September 1850"
print(f'{customer["name"]} was born on {customer["birthdate"]}')

# exercise
# Spell an input phone number

# My version
# Uses actual integers, and does not check for invalid characters
# requires integer conversion
# if you type a character it will crash

speller = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

phoneNumber = input("Enter Phone Number: ")
outputString = ''
for number in phoneNumber:
    outputString = outputString + " " + speller[int(number)]
print(outputString)

# Mosh's version
# Uses characters as dictionary index and uses .get() method to check for illegal characters
# doesn't require integer conversion
# doesn't crash if you input illegal stuff

speller = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

phoneNumber = input("Enter Phone Number: ")
outputString = ''
for number in phoneNumber:
    outputString += speller.get(number, "!") + " "
print(outputString)

# My corrected, type checking version
# uses .isdigit() method for strings
# works only on positive numbers (to be expected)
# removes whitespaces
# checks and corrects the plus sign to a double zero (how neat)

print()
headerMessage = "This version handles any usual weird phone formats except extensions with # or *"
print("~" * len(headerMessage))
print(headerMessage)
print("That includes +02 etc. area codes and (699)etc. carrier codes")
print("~" * len(headerMessage))

speller = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

phoneNumber = input("Enter Phone Number: ")
if phoneNumber.find(" ") is not -1:             # strips white spaces
    print("Found Spaces!")
    phoneNumber = phoneNumber.replace(" ","")
if phoneNumber.find("(") or phoneNumber.find(")") is not -1:             # strips white spaces
    print("Found Brackets!")
    phoneNumber = phoneNumber.replace("(","")
    phoneNumber = phoneNumber.replace(")", "")
if phoneNumber[0] == "+":                       # replaces + with 00
    print("Found Plus!")
    phoneNumber = phoneNumber.replace("+","00")
    print(f"Formatting...{phoneNumber}")
if phoneNumber.isdigit():
    outputString = ''
    for number in phoneNumber:
        outputString = outputString + speller[int(number)] + " "
    print(outputString)
else:
    print("Invalid Number!")