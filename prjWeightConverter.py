weight = float(input("Enter weight: ")) # convert string to float for math later
units = input("Select (K)ilograms or (P)ounds: ")

if units.upper() == 'K':                # convert input to uppercase to make case insensitive
    print(f"That's {weight*2.205}lbs.")
elif units.upper() == 'P':
    print(f"That's {weight*0.454}kg.")
else:
    print("Invalid Units Selected")