message = input(">")
words = message.split(" ") # outputs a list, separated by the argument character
emojis = {
    ":)":"😀",
    ":(":"😟"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " " # gets the matching string in the dictionary, uses the input if not found (2nd arg)
print(output)