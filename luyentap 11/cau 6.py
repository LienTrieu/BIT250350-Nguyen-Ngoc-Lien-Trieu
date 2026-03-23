n = int(input("nhap so nguoi: "))
people = {}
for i in range(n):
    name = input(f"Nhap ten nguoi {i+1}: ")
    age = int(input(f"nhap tuoi {name}: "))
    people[name] = age
avg_age = sum(people.values()) / len(people)
print(f"tuoi trung binh: {avg_age:.2f}")
items = list(people.items())
for i in range(len(items)):
    max_idx = i
    for j in range(i + 1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j
    items[i], items[max_idx] = items[max_idx], items[i]
sorted_people = dict(items)
print("danh sach sau khi sap xep:")
for name, age in sorted_people.items():
    print(f"{name}: {age}")