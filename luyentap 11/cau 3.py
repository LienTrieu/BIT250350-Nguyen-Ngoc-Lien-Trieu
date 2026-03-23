n = list(map(int, input("nhap so: ").split()))
nguoi = []
for i in n:
    if i % 2 == 0:
        nguoi.append(i)
print("so chan :", nguoi)
print("tong cac so chan:", sum(nguoi))
