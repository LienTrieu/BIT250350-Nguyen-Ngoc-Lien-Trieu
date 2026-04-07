#bai 1
a = 10
b = 3.5
c = "Hello"
print(a)
print(b)
print(c)
#bai 2
PI = 3.14
r = 5
chu_vi = 2 * PI * r
print("Chu vi hình tròn:", chu_vi)
#bai 3
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
print("Tổng:", x + y)
print("Hiệu:", x - y)
print("Tích:", x * y)
if y != 0:
    print("Thương:", x / y)
else:
    print("Không thể chia cho 0")
#bai 4
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(3, 5))
#bai 5
name = "An"
age = 20
average_score = 8.5
print(type(name))
print(type(age))
print(type(average_score))
age_next_year = age + 1
doubled_score = average_score * 2
print(name, age, average_score)
print(age_next_year, doubled_score)
#bai 6
def is_even(n):
    return n % 2 == 0
print(is_even(4))
print(is_even(7))
#bai 7
a = int(input("Nhập số 1: "))
b = int(input("Nhập số 2: "))
c = int(input("Nhập số 3: "))
print("Số lớn nhất:", max(a, b, c))
#bai 8
def greet(name="Student"):
    print("Hello,", name + "!")
greet()
#bai 9
age = int(input("Nhập tuổi: "))
if 1 <= age <= 120:
    print("Tuổi hợp lệ")
else:
    print("Tuổi không hợp lệ")
#bai 10
s = input("Nhập chuỗi: ")
count = s.count('a')
print("Số lần xuất hiện của 'a':", count)
##bai 11
c = float(input("Nhập nhiệt độ C: "))
f = c * 9/5 + 32
print(f"Nhiệt độ F: {f:.2f}")
#bai 12
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))
bmi = weight / (height * height)
print(f"BMI: {bmi:.2f}")
#bai 13
try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    result = a / b
    print("Kết quả:", result)
except ZeroDivisionError:
    print("Không thể chia cho 0")
except ValueError:
    print("Dữ liệu không hợp lệ")
#bai 14
import math
n = float(input("Nhập số: "))
if n < 0:
    print("Không thể tính căn bậc hai của số âm")
else:
    print("Căn bậc hai:", math.sqrt(n))
#bai 15
for i in range(3):
    name = input("Nhập tên sinh viên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))
    avg = (toan + ly + hoa) / 3
    print(f"{name} - Điểm trung bình: {avg:.2f}")