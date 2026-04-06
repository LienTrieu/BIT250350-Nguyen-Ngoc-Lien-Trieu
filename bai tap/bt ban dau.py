#bt1
names = []
for i in range(5):
    name = input(f"nhap ten thu {i+1}: ")
    names.append(name)
print("danh sach ban dau:", names)
del names[1]
print("danh sach sau khi xoa:", names)
#bt2
import math
arr = list(map(int, input("nhap so: ").split()))
odd_numbers = [x for x in arr if x % 2 != 0]
print("so le:", odd_numbers)
print("tong so luong so le:", len(odd_numbers))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers = [x for x in arr if is_prime(x)]
print("so nguyen to:", prime_numbers)
#bt3
books = [30000, 50000, 100000]
with open("books.txt", "w") as f:
    total = 0
    for i, price in enumerate(books, start=1):
        f.write(f"Book {i}:{price}\n")
        total += price
    f.write(f"Tong:{total}")
#bt4
layers = {
    "layer-11": {
        "layer-21": 90,
        "layer-22": {
            "layer-31": 43
        }
    },
    "layer-12": 35
}
print(layers["layer-12"])
print(layers["layer-11"]["layer-22"]["layer-31"])