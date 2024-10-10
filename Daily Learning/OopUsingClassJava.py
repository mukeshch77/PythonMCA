#object oriented programming/ use of class in java

class Dog():
    #Class attribute (shared by all instances)
    species= "Canis familiaris"

    #constructor (initializer)
    def _init_(self, name, age):
        #instance attributes (unique to each instance)
        self.name = name
        self.age = age
    #instance method
    def bark(self):
        return f"{self.name} says woof!"

    #another instance method 
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    

class Cat:
    #Class attribute (shared by all instances)
    species= "Cat species"

    #constructor (initializer)
    def _init_(self, name, age):
        #instance attributes (unique to each instance)
        self.name = name
        self.age = age
    #instance method
    def meu(self):
        return f"{self.name} says meu!"

    #another instance method 
    def get_age(self):
        return f"{self.name} is {self.age} years old."

#creating instances (0bjects) of the dog class
dog1 = Dog("Buddy",3)
dog2 = Dog("Charlie", 5)
cat1 = Cat("cat1",2)

#accessing attributes and methods
print(dog1.bark())  #buddy says woof!
print(dog2.get_age())  #charlie is 5 years old
print(dog1.species)

print("===")
#object oriented programming/ use of class in java

class Dog:
    #Class attribute (shared by all instances)
    species= "Canis familiaris"

    #constructor (initializer)
    def _init_(self, name, age):
        #instance attributes (unique to each instance)
        self.name = name
        self.age = age
    #instance method
    def bark(self):
        return f"{self.name} says woof!"

    #another instance method 
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    

class Cat:
    #Class attribute (shared by all instances)
    species= "Cat species"

    #constructor (initializer)
    def _init_(self, name, age):
        #instance attributes (unique to each instance)
        self.name = name
        self.age = age
    #instance method
    def meu(self):
        return f"{self.name} says meu!"

    #another instance method 
    def get_age(self):
        return f"{self.name} is {self.age} years old."

#creating instances (0bjects) of the dog class
dog1 = Dog("Buddy",3)
dog2 = Dog("Charlie", 5)
cat1 = Cat("cat1",2)

#accessing attributes and methods
print(cat1.meu())  #buddy says woof!
print(cat1.get_age())  #charlie is 5 years old
print(cat1.species)