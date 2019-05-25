# on lists

names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names[2:]) # print all from starting index

print(names[2:4]) # from start till end index except for the end index

names[0] = "Jon" # editing list entries
print(names)

# exercise
# find biggest number in a list

# My solution
numbers = [1,36,7,12,19,26,49,21,5,59]
recordCountOfSmallerNumbers = 0
recordHolder = 0


for currentNumber in numbers:                           #cycles through all numbers
    print(f"Current Number: {currentNumber}")           #current number is set
    countOfSmallerNumbers = 0                           #resets countOfSmallerNumbers
    for comparisonNumber in numbers:                    #loops again through the list
        if currentNumber > comparisonNumber:            #compares current number to the current comparison number
            countOfSmallerNumbers += 1                  #increments count of numbers that are smaller
    print(f"{countOfSmallerNumbers} numbers are smaller than {currentNumber}") #end of second list loop
    if countOfSmallerNumbers > recordCountOfSmallerNumbers: #checks if the current result is higher than the record
        recordCountOfSmallerNumbers = countOfSmallerNumbers #updates the record if true
        print(f"Current Record Holder is: {currentNumber}")
        recordHolder = currentNumber                        #records the number that set the record
print(f"The largest number is {recordHolder}")              #after looping through all numbers, prints the record holder


# Mosh's solution
# much much MUCH easier. I think like an idiot.
print()
print("Mosh's algorithm")

max = numbers[0]        #assume 1st number is the biggest. Works with max = 0 too.
for number in numbers:  #loop through all numbers
    if number > max:    #check if current number is bigger than max
        max = number    #if so, update max
        print(f"Current Max: {max}")
print(max)              #print fucking max




# Dafuck happened here...? Why didn't I come up with the much simpler solution?