import csv
name = input("Tên: ")
age = input("Tuổi: ")
emp_id = input("ID: ")
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"{name}, {age}, {emp_id}")
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "ID"])
    writer.writerow([name, age, emp_id])
print("luu file")