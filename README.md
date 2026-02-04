#bai 1
n = int(input("Nhập số từ 1 đến 9: "))
if 1 <= n <= 9:
    for i in range(1, 10):
        print(f"{n} x {i} = {n*i}")
else:
    print("Số không hợp lệ")
#bai 2
n = int(input("Nhập số dương: "))
if n < 2:
    print("Không phải số nguyên tố")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Không phải số nguyên tố")
            break
    else:
        print("Là số nguyên tố")
#bai 3
n = int(input("Nhập n: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
#bai 4
n = input("Nhập số: ")
tong = sum(int(ch) for ch in n)
print("Tổng các chữ số:", tong)
#bai 5
chuoi = input("Nhập chuỗi: ")
ky_tu = input("Nhập ký tự cần đếm: ")
print("Số lần xuất hiện:", chuoi.count(ky_tu))
#bai 6
def giaithua(n):
    if n == 0:
        return 1
    return n * giaithua(n - 1)

n = int(input("Nhập số: "))
print("Giai thừa:", giaithua(n))
#bai 7
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print("USCLN:", a)
#bai 8
n = int(input("Nhập số dương: "))
dao = 0

while n > 0:
    dao = dao * 10 + n % 10
    n //= 10

print("Số sau khi đảo:", dao)
#bai 9
n = int(input("Nhập số nguyên dương 5 chữ số: "))

max_digit = 0
while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n //= 10

print("Chữ số lớn nhất là:", max_digit)
#bai 10
def tong(n):
    if n == 1:
        return 1
    return n + tong(n - 1)

n = int(input("Nhập n: "))
print("Tổng từ 1 đến", n, "là:", tong(n))
#bai 11
dtb = float(input("Nhập điểm trung bình: "))

if dtb >= 8:
    print("Xếp loại: Giỏi")
elif dtb >= 6.5:
    print("Xếp loại: Khá")
elif dtb >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")
#bai 12
n = int(input("Nhập n: "))
s = 0

for i in range(1, n + 1, 2):
    s += i

print("Tổng các số lẻ từ 1 đến", n, "là:", s)
#bai 13
password = ""

while password != "python123":
    password = input("Nhập mật khẩu: ")

print("Đúng mật khẩu! Đăng nhập thành công.")
#bai 14
n = int(input("Nhập n: "))

if n < 2:
    print(n, "không phải số nguyên tố")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break        
    if is_prime:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải số nguyên tố")
#bai 15
n = int(input("Nhập số nguyên dương: "))
s = 0

while n > 0:
    s += n % 10
    n //= 10

print("Tổng các chữ số là:", s)
