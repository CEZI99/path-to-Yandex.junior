# Сортировка Пузырьком.
a = [123, 4, 2, 87, 12, 3, 25]
n = len(a)
for i in range(0, n - 1):
    for j in range(0, n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)