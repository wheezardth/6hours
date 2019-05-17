class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hey, my name is {self.name} and I'm an object, not a Person.")


dude = Person("Doyle")

dude.talk()