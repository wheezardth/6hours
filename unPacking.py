coordinates = (1, 2, 3)

# coordinates[0] * coordinates[2]
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
# nothing new

print(x,y,z)
x = y = z = 0
print(x,y,z)
x, y, z = coordinates #unpacking
print(x,y,z)
