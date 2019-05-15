# Python is a *string* of characters, so item will hold a successive character of that string
# This is SO easy
for item in "Python":
    print(item)

# next up we define a list by using []
# we don't even have to name the shit...

for item in ["Dude","this","is","rad","."]:
    print(item)

# next up, we define a range() which creates an object
# range has a start, end and step arguments, and is overloaded
# empty print() spits out CRLF
# whitespaces between arguments are favorable

print()
for item in range(10):
    print(item)

print()
for item in range(5, 10):
    print(item)

print()
for item in range(2, 12, 2):
    print(item)

# now an example of adding stuff together from a list
# print can print lists with no additional arguments
print()
print("Shopping Cart Calculator")

cart = [10, 25, 40, 2.99]
tally = 0
print(cart)

for itemPrice in cart:
    tally += itemPrice
    print(f"Current tally: {tally}")
print(f"Total Cost: {tally}")
