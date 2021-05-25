# Метод слияния двух упорядоченных списков
a = [1, 4, 5, 12, 34]
b = [2, 5, 12, 54, 54]
c = []

n = len(a)
m = len(b)

i = 0
j = 0

while i < n and j < m:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1

    else:
        c.append(b[j])
        j += 1

c += a[i:] + b[j:]
print(c)
print(f"")