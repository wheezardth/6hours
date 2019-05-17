# inheritance is a method for reusing code
# D.R.Y. Principle = Don't Repeat Yourself (twice the debugging)

class Pidgeon:
    def walk(self):                 # both classes have the same method
        print("Pidgeion walks.")


class Chicken:
    def walk(self):                 # this is redundant and should be avoided. Also it's ugly.
        print("Chicken walks.")


class Mammal:
    def walk(self):                 # this will be the parent class for inheritance demo
        print("walk-walk-walk")


class Dog(Mammal):                  # the name in parenthesis is the PARENT class
    pass                            # the pass keyword means ignore this row.
                                    # Used because Python doesn't like empty classes

class Cat(Mammal):
    def meow(self):
        print("🐱    🐱    🐱")


dog = Dog()
wanda = Cat()

dog.walk()

wanda.walk()                       # the cat class instance (object) can both walk (inherited) and meow (private)
wanda.meow()