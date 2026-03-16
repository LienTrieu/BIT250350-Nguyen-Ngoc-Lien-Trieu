class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
    def __eq__(self, other):
        return self.diem == other.diem
sv1 = SinhVien("thang", 9)
sv2 = SinhVien("thai",9)
if sv1 == sv2:
    print("hai sinh vien bang diem")
else:
    print("hai sinh vien khac diem diem")