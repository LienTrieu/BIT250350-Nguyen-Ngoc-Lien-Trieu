lst = []
n = int(input("nhap so phan tu : "))
for i in range(n):
    lst.append(int(input("nhap so: ")))
print("danh sach:", lst)
k = int(input("nhap k: "))
print("so lan xuat hien:", lst.count(k))
tong = 0
for x in lst:
    if x > 1:
        la_snt = True
        for i in range(2, x):
            if x % i == 0:
                la_snt = False
                break
        if la_snt:
            tong += x
print("tong so nguyen to:", tong)
lst.sort()
print("sau khi sap xep:", lst)
lst.clear()
print("sau khi xoa:", lst)