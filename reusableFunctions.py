def emoji_converter(input):
    words = input.split(" ")  # outputs a list, separated by the argument character
    emojis = {
        ":)":"😀",
        ":(":"😟"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji_converter(input(">")))
