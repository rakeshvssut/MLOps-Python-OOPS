# Initiate a class

class employee:
    def __init__(self):
        print("Started executing attribute/deta")
        self.id = 111
        self.salary = 50000
        self.designation = "DevOps Engineer"
        print("Started attribute/deta have been initiated")
    # Method/Attribute

    def travel(self, destination):
        print("This travel function is called manually")
        print(F"Employee is travelling to destination {destination}")


# Create a Object/Instance
sam = employee()

# calling a method
sam.travel("kerala")

# Priting the attribute
# print(sam.salary)
