#cau 1
def thong_tin_tuple(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat
t = (3, 5, 7, 1, 9)
print(thong_tin_tuple(t))
#cau 2
def diem_trung_binh(ds):
    tong = sum(ds.values())
    return tong / len(ds)
sinh_vien = {
    "An": 8,
    "Binh": 7,
    "Chi": 9
}
print("Điểm trung bình:", diem_trung_binh(sinh_vien))
#cau 3
def kiem_tra_key(dic, key):
    if key in dic:
        print("Key tồn tại")
    else:
        print("Key không tồn tại")
sinh_vien = {"An":8, "Binh":7, "Chi":9}
kiem_tra_key(sinh_vien, "An")
#cau 4
class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
hoa1 = Hoa("Hoa hồng", "Đỏ")
print("Tên hoa:", hoa1.ten)
print("Màu:", hoa1.mau)
#cau 5
class Product:
    def __init__(self, price):
        self.set_price(price)
    def get_price(self):
        return self._price
    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Giá phải lớn hơn 0")
    def __str__(self):
        return f"Price: {self._price}"
p = Product(100)
print(p)