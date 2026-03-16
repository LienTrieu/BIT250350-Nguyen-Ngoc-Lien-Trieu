class animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print("sound")
class Dog(animal):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print("gau gau")
dog1 = Dog("HEhe")
print("ten:", dog1.name)
dog1.sound()