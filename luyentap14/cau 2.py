n = int(input("nhap n: "))
print("hinh 1:")
for i in range(n):
    for j in range(n):
        print("*", end="  ")
    print()
print("hinh 2:")
for i in range(1, n+1):
    for j in range(i):
        print("*", end="  ")
    print()
print("hinh 3:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="  ")
    print()
print("hinh 4:")
for i in range(1, n+1):
    print("  " * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()
print("hinh 5:")
for i in range(n):
    for j in range(n):
        if j == 0 or i == n-1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("hinh 6:")
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("hinh 7:")
for i in range(n):
    for j in range(n):
        if j == n-1 or i == n-1 or j == n-i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("hinh 8:")
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("* ", end="")
    print()
print("hinh 9:")
for i in range(n):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    elif i == n - 1:
        print("* " * n)
    else:
        print("*" + " " * (2 * i - 1) + "*")
print("hinh 10:")
for i in range(n):
    print(" " * i, end="")
    if i == 0:
        print("* " * n)
    elif i == n - 1:
        print("*")
    else:
        print("*" + " " * (2 * (n - i - 1) - 1) + "*")
