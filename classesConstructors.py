# a constructor is a function that gets called at the creation time of an object
# self is a reference to the current object
# the __init__  name is special and indicates the function is THE constructor

class Point:
    def __init__(self, x_init_coord=None, y_init_coord=None):  # None keyword allows to create object w.o init coords
        self.x = x_init_coord       # init values can be set via arguments to the class
        self.y = y_init_coord
        self.z = 50                 # or can be static, if so desired
        self.c = None               # it can also be a None

    def move(self):     #methods
        print("move")

    def draw(self):
        print("draw")


# Point()               # calling the class like a function creates a new object

point1 = Point(10,20)
print(point1.x)
print(point1.y)
print(point1.z)

point2 = Point(25,45)
print(point2.x)
print(point2.y)
print(point2.z)

point3 = Point()
print(point3.x)
print(point3.y)
print(point3.z)