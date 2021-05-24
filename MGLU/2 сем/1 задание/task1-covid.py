# Задача № 1
# Подготовить программу считывающую файл данных о заражении COVID-19,
# подготовить диаграмму с графиками развития эпидемии для 5 стран с наибольшим количеством зараженным.
# Использовать для подготовки библиотеки Pandas и Mathplot. Данные можно взять из общедоступных источников

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('covid-1919.csv', delimiter=';')
fig = plt.figure()
# Получение данных из файла:
os_x = [x[0:5] for x in data.date.values]

usa_y = [int(y) for y in data.Usa.values]
india_y = [int(y) for y in data.India.values]
brazil_y = [int(y) for y in data.Brazil.values]
france_y = [int(y) for y in data.France.values]
russia_y = [int(y) for y in data.Russia.values]
# Построение графиков
usa = plt.plot(os_x, usa_y, color="black")
india = plt.plot(os_x, india_y, color="yellow")
brazil = plt.plot(os_x, brazil_y, color="orange")
france = plt.plot(os_x, france_y, color="blue")
russia = plt.plot(os_x, russia_y, color="red")
# Настройка графиков
plt.ylim(0, 10000000)
plt.title("График развития заражений COVID-19 в 2020")
plt.xlabel("День/месяц в 2020")
plt.ylabel("Количество заражений")
plt.grid()
plt.legend((usa[0], india[0], brazil[0], russia[0], france[0]), ("США", "Индия", "Бразилия", "Россия", "Франция"))
plt.show()
