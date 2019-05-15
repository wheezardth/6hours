first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
# this is a formatted string
# the f prefix of defines a formatted string
# the curly braces act as placeholders, this avoids concatenation
msg = f'{first} [{last}] is a coder'
print(msg)