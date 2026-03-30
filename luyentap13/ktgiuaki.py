#bai 1
n = int(input("nhap so:"))
if n < 0 :
    print("loi")
else:
    print("can bac 2:",n**(1/2))
#bai 2
n = input("nhap chuoi: ")
print("do dai chuoi:", len(n))
print("so ki tu 'a':", n.count('a'))
#bai 3
tong = 0
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        tong += i
print("tong cac so chan:", tong)
#bai 4
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
n = int(input("nhap so: "))
print("giaithua:", giai_thua(n))
#bai 5
class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    def __str__(self):
        return f"ten hoa: {self.name}, mau: {self.color}"
f = Flower("hoa hong", "do")
print(f)
#bai 6
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
a = [5, 2, 9, 1, 3]
print("sau khi sx:", bubble_sort(a))