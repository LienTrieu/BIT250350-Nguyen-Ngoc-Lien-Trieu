#bai 1
pi = 3.14
n = float(input("nhap so:"))
print("chu vi hinh tron:",2*n*pi)
#bai 2
a = int(input("nhap so:"))
b = int(input("nhap so:"))
print("tong:", a+b)
print("hieu 1:", a-b)
print("hieu 2:", b-a)
print("tich:", a*b)
#bai 3
class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def set_name(self, name):
        self.name = name
    def set_price(self, price):
        self.price = price
book = Book("Conan", 200.0)
print("Price:", book.get_price())