birth_year = input("Birth Year: ")
age = 2019 - int(birth_year)
print(age)

lied = input("Did you lie? ")
print(type(lied))
nonTruth = bool(lied)
print(type(nonTruth))
print(nonTruth)

#int() converts to int
#float() converts to float
#bool() converts to bool (any string is True, empty string is False