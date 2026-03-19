import os
def get_filename(path):
    return os.path.basename(path)
def get_name_only(path):
    return os.path.splitext(os.path.basename(path))[0]
def factorial(n):
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt
while True:
    choice = input("Chọn: ")
    if choice == "1":
        path = input("Nhập đường dẫn: ")
        print("Tên file:", get_filename(path))
        print("Tên không đuôi:", get_name_only(path))
    elif choice == "2":
        s = input("Nhập chuỗi: ")
        char = input("Nhập ký tự: ")
        print(s.count(char))
    elif choice == "3":
        n = int(input("Nhập số: "))
        print(factorial(n))
    elif choice == "0":
        break
    else:
        print("Lựa chọn không hợp lệ!")