class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

class Tiger:

    species = "big cat"

    def __init__(self, name, food):
        self.name = name
        self.food = food

    def hungry(self):
        return "{} is getting hungry for {}".format(self.name,self.food)

    def home(self, area):
        return "{} lives in {}".format(self.name, area)

kitty = Tiger("Kitty", "Zebra")
felix = Tiger("Felix", "Gazelle")

print("{} is a {}!".format(felix.name, felix.__class__.species))
print("{} is also a {}!".format(kitty.name, kitty.__class__.species))

print("Kitty's favoured food is {}".format(kitty.food))
print("Felix's favoured food is {}".format(felix.food))

print(kitty.hungry())
print(felix.home("the woods"))