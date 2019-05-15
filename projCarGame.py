# https://youtu.be/_uQrJ0TkZlc?t=5516


print("*** Car Game Deluxe ***")
print("***    My version   ***")

game_running = True

while game_running == True:
    command = input(">")

    if command.lower() == "help":
        print("start > Starts the car")
        print("stop  > Stops the car")
        print("quit  > Exits the game")
    elif command.lower() == "start":
        print("Car Started! Ready to GO!")
    elif command.lower() == "stop":
        print("Car Stopped...")
    elif command.lower() == "quit":
        print("Bye bye!")
        game_running = False
    else:
        print("Type help for valid commands")

print("*** Car Game Deluxe ***")
print("***  Mosh's version ***")

# while commmand != quit: # that was the original. Variable declaration in loop initialization possible!
while True:
    command = input(">").lower() # lower-caseify at input, treat input() as a string straight away!

    if command == "help":        # triple quote, everything is literal, including indentations & new line
        print("""start - to start the car         
stop  - to stop the car
quit  - to quit""")
    elif command == "start":
        print("Car Started! Ready to GO!")
    elif command == "stop":
        print("Car Stopped...")
    elif command == "quit":
        break
    else:
        print("Type help for valid commands")

print("*** Car Game Deluxe ***")
print("***  My extension of Mosh's version ***")
# still can be tricked to start twice if you enter a different command between same commands
# because we don't save the states of the car

old_command = "nada"
while True:
    command = input(">").lower()
    if old_command == command and not command == "help":
        print("That already happened")
    else:
        old_command = command
        if command == "help":
            print("""
start - to start the car         
stop  - to stop the car
quit  - to quit
                  """)
        elif command == "start":
            print("Car Started! Ready to GO!")
        elif command == "stop":
            print("Car Stopped...")
        elif command == "quit":
            break
        else:
            print("Type help for valid commands")

print("*** Car Game Deluxe ***")
print("***  My second version of the extension of Mosh's version ***")
# still can be tricked into stopping the car before it is started because car state is still not saved
# also if you type an invalid command twice it doesn't offer help the second time
# verdict: Over-engineered in the wrong way. K.I.S.S.

car_state = "nada"
while True:
    command = input(">").lower()
    if car_state == command:
        print("That already happened")
    else:
        old_command = command
        if command == "help":
            print("""
    start - to start the car         
    stop  - to stop the car
    quit  - to quit
                  """)
        elif command == "start":
            print("Car Started! Ready to GO!")
            car_state = command
        elif command == "stop":
            print("Car Stopped...")
            car_state = command
        elif command == "quit":
            break
        else:
            print("Type help for valid commands")

print("*** Car Game Deluxe ***")
print("***  Mosh's extension of his version ***")

car_started = False
while True:
    command = input(">").lower()

    if command == "help":
        print("""
start - to start the car         
stop  - to stop the car
quit  - to quit
              """)
    elif command == "start":
        if car_started:
            print("Engine running...")
        else:
            print("Car Started! Ready to GO!")
            car_started = True
    elif command == "stop":
        if not car_started:
            print("Can't get stopped-er than that.")
        else:
            print("Car Stopped...")
            car_started = False
    elif command == "quit":
        break
    else:
        print("Type help for valid commands")