def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(arr[j]) < len(arr):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"buoc {i}: {arr}")
arr =[]
for i in range(5):
    s = input(f"nhap chuoi {i+1}:")
    arr.append(s)
insertion_sort(arr)
print("ketqua:",arr)