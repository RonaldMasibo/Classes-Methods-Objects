
class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def displayinfo(self):
        print("Hello. My name is " + self.name)
        print("I am " + self.age + " years old")
        print("My gender is " + self.gender)