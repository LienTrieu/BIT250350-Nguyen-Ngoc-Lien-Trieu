def bubble_sort(a):
    n = len(a)
    buoc = 1
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if len(a[j]) < len(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                print(f"Bước {buoc}: {a}")
                buoc += 1
a = []
for i in range(5):
    s = input(f"Nhập chuỗi{i + 1}: ")
    a.append(s)
print("Danh sách ban đầu:", a)
bubble_sort(a)
print("Danh sách khi sắp xếp:", a)