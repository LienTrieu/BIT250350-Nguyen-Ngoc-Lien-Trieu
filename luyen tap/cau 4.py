s = input('Nhap chuoi: ')
hoa = 0
thuong = 0
so = 0
dac_biet = 0
khoang_trang = 0
nguen_am = 0
phu_am = 0
for c in s:
    if c.isupper():
        hoa += 1
    if c.islower():
        thuong += 1
    if c.isdigit():
        so += 1
    if c.isspace():
        khoang_trang += 1
    if c.lower() in 'aeiou':
        nguen_am +=1
    elif c.isalpha():
        phu_am += 1
    if not c.isalnum() and not c.isspace():
        dac_biet += 1
print('Chu hoa: ', hoa)
print('Chu thuong: ', thuong)
print('So: ', so)
print('Ki tu dac biet: ', dac_biet)
print('Ki tu khoang trang: ', khoang_trang)
print('Nguyen am: ', nguen_am)
print('Phu am: ', phu_am)