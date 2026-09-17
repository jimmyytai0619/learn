class Dog():
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.breed} says Woof!"

print(my_dog := Dog("Labrador", 3).bark())

#----------
class Circle():

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(5)
my_circle.circumference()
my_circle.radius
#print(my_circle.area)
#print(my_circle.circumference())
#print(my_circle.radius)

#----------
class Animal():

    def __init__(self):
        print ("Animal created")

    def who_am_i(self):
        print ("I am an animal")

    def eat(self):
        print ("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print ("Dog created")

    def eat(self):
        print ("I am a dog and I am eating")

    def bark(self):
        print ("Woof!")

mydog = Dog()
mydog.who_am_i()
mycat = Animal()
mycat.eat()
mycat.who_am_i()

mydog.bark()

#----------

class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
       #the self.height = height means my_cylinder.height = 2

    def volume(self):
        return Cylinder.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * Cylinder.pi * self.radius * self.height + 2 * Cylinder.pi * (self.radius ** 2)

my_cylinder = Cylinder(2, 3)
print(my_cylinder.volume())
print(my_cylinder.surface_area())