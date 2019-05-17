# classes define custom data types that represent more complex structures
# Default python naming convention: email_client_handler
# Pascal naming convention: EmailClientHandler
# classes in python are named using the Pascal naming convention

# classes are defined using the class keyword
# classes are blueprints of complex structures
# objects are the -actual- instances of classes, e.g. instances of those blueprints
# attributes are like variables for specific objects


class Point:
    def move(self):     #methods
        print("move")

    def draw(self):
        print("draw")


# Point()               # this creates a new object
point1 = Point()        # we now store this in a variable
point1.x = 10           # attributes  do not need to be declared in advance in the class definition?
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)