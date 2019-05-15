i = 1
while i<= 5:
    print('*' * i)
    i += 1

secret = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess:"))
    guess_count += 1
    if guess == secret:
        print("You won!")
        break
else: # if the while loop completes without a break statement
    print("You lost :(")
print("Game Over")