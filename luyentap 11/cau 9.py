def input_matrix(r, c):
    matrix = []
    for i in range(r):
        row = []
        for j in range(c):
            val = input(f"Nhập phần tử [{i}][{j}]: ")
            if val == "":
                raise ValueError("Không được để trống")
            row.append(int(val))
        matrix.append(row)
    return matrix
r = int(input("Số hàng: "))
c = int(input("Số cột: "))
try:
    print("Nhập ma trận A:")
    A = input_matrix(r, c)
    print("Nhập ma trận B:")
    B = input_matrix(r, c)
    C = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    print("Ma trận tổng:")
    for row in C:
        print(row)
except ValueError as e:
    print("Lỗi:", e)