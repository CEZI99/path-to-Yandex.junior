# Быстрая сортировка слиянием (merge sort)
def merge(a, b):    # Метод слияния двух упорядоченных списков
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
    return c

# функция деления списка и слияния списков в общий отсортированный список
def split_and_merge_list(a):
    N1 = len(a) // 2
    a1 = a[:N1]     # деление массива на два примерно равной длины

    a2 = a[N1:]

    if len(a1) > 1: # если длина 1-го списка больше 1, то делим дальше
        a1 = split_and_merge_list(a1)
    if len(a2) > 1: # если длина 2-го списка больше 1, то делим дальше
        a2 = split_and_merge_list(a2)

    return merge(a1, a2)   # слияние двух отсортированных списков в один


a = [9, 5, -3, 4, 7, 8, -8]
a = split_and_merge_list(a)

print(a)
