n = int(input("nhap n: "))
print("hinh 1:")
for i in range(n):
    for j in range(n):
        print(1, end="  ")
    print()
print("hinh 2:")
for i in range(n):
    for j in range(1, n+1):
        print(j, end="  ")
    print()
print("hinh 3:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="  ")
    print()
print("hinh 4:")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end="  ")
    print()
print("hinh 5:")
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == i or i == n:
            print(j, end="  ")
        else:
            print(" ", end="  ")
    print()
print("hinh 6:")
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n - i - 1:
            print(j+1, end="  ")
        else:
            print(" ", end="  ")
    print()
print("hinh 7:")
for i in range(1, n+1):
    print("  " * (n - i), end="")
    for j in range(i):
        print(i, end="   ")
    print()
print("hinh 8:")
for i in range(1, n + 1):
    print("   " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="  ")
    for j in range(i - 1, 0, -1):
        print(j, end="  ")
    print()
print("hinh 9:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    if i < n:
        print("1", end="")
        print("  " * (2 * i - 3), end="  ")
        if i > 1:
            print("1", end="")
    else:
        for j in range(1, n + 1):
            print(j, end=" ")
        for j in range(n - 1, 0, -1):
            print(j, end=" ")
    print()