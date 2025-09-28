# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# # Derived class
# class Dog(Animal):

#     def speak(self):
#         print(f"{self.name} barks")


# # Create a instance for animal
# animal = Animal("Generaic Animal")

# animal.speak()


# # Create a instance for dog
# doggy = Dog("Buddy")

# doggy.speak()


# Super Keyword


class Animal:

    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        self.speak = {f"{self.name} makes a sound"}


class Dog(Animal):

    def __init__(self, bread):
        super().__init__()
        self.bread = bread

    def taste(self):
        super().speak()
        print(f"{self.name} barks . it is {self.bread}")


doggy = Dog("German Suffered")

doggy.taste()
