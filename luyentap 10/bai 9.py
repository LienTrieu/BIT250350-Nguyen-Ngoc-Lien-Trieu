class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def set_name(self, name):
        if not name:
            raise ValueError("Tên không hợp lệ")
        self._name = name
    def set_age(self, age):
        if age < 0:
            raise ValueError("Tuổi phải >= 0")
        self._age = age
    def __str__(self):
        return f"{self._name} - {self._age}"
    def say_hello(self):
        return "Hello!"
    @classmethod
    def create_default(cls):
        return cls("Unknown", 0)
    @staticmethod
    def is_adult(age):
        return age >= 18
    def __eq__(self, other):
        return self._name == other._name and self._age == other._age
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def __str__(self):
        return f"{self._name} - {self._age} - {self.grade}"
# Test
p1 = Person("Trieu", 18)
p2 = Person.create_default()
s1 = Student("Thoang", 19, "A")
print(p1)
print(p2)
print(s1)
print(p1 == p2)
print(Person.is_adult(20))