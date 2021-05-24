# 3. Написать программу,
# создающую список 100 случайных значений в диапазоне от -100 до 100
# и подсчитывающую среднее значение всех положительных значений. Результат вывести на экран.

import random
numlst = []

count = 0
while count < 101:
    x = random.randrange(-101, 101)
    numlst.append(x)
    count += 1

print(numlst)

s = 0
q = 0

for i in range(len(numlst)):
    if numlst[i] > 0:
        s += numlst[i]
        q += 1

result = s / q

print(result)

end = input()