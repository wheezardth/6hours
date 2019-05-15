# AND   all lower case btw
# OR    also can string logical operators
# NOT

name = input("Put your name in: ")
if len(name) > 8:
    print("That's a weird name...")
elif len(name) <= 2:
    print("That's not a name, idjit!")
else:
    print(f'Nice name, {name}!')

has_high_income = True
has_good_credit = True

has_criminal_record = False

if has_good_credit and has_high_income:
    print(f'{name}, you are eligible for a loan')

if has_high_income and not has_criminal_record:
    print(f'{name}, you are also eligible for a line of coke')
else:
    print(f"Sorry {name}, can't do...")
