class SinhVien:
    count = 0
    def __init__(self, ten):
        self.ten = ten
        SinhVien.count += 1
    @classmethod
    def dem_sinh_vien(cls):
        return cls.count
sv1 = SinhVien("thang")
sv2 = SinhVien("thai")
sv3 = SinhVien("thoang")
print("so sv: ",SinhVien.dem_sinh_vien())
