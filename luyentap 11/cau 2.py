def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif len(arr[mid]) < len(target):
            right = mid - 1
        else:
            left = mid + 1
    return -1
arr = ["1", "22", "333", "4444", "5555"]
target = input("nhap chuoi can tim: ")
pos = binary_search(arr, target)
if pos != -1:
    print("tim vi tri:", pos)
else:
    print("khong tim thay")