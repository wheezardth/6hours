# finally...

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day!")

temperature = -5.762

print(f'The temperature is {temperature}°C')
if temperature > 32.0:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature < 5.0:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day!")


house_cost = 1000000
good_credit = False
rateGood = 0.1
rateBad = 0.2

if good_credit:
    print(f'Down payment is {house_cost * rateGood} EUR')
else:
    print(f'Down payment is {house_cost * rateBad} EUR')

down_payment = 0

if(good_credit):
    down_payment = 0.1 * house_cost
else:
    down_payment = 0.2 * house_cost
print(f'Down payment is {down_payment} EUR')

