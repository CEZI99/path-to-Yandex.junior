#   Задача № 3
# Подготовить программу чтения и анализа страницы по заданному адресу,
# подсчитывающую количество упоминаний каждого слова.
# Для анализа выбирается страница с не менее чем 3Кб текста для анализа,
# элементы навигации и оформления в анализе не участвуют.
# Результаты анализа сохраняются в CSV-файле, отсортированном по убыванию
# или демонстрируются на столбчатой диаграмме (первые 200 слов).

import requests, io, re, operator
import lxml.html as html
from lxml import etree
import matplotlib.pyplot as plt
import matplotlib as mpl
words_dict = {}
r = requests.get(url="https://www.levada.ru/2020/11/02/koronavirus-strahi-i-mery/")
html_body = html.fromstring(r.content)
text_from_body = html_body.xpath('//*[@id="post-23783"]')
# создание регулярного выражения patern для поиска слов в содержимом text_from_body
for elem in text_from_body:
    patern = etree.tostring(elem, encoding = 'unicode')
    patern = re.sub(r'<[^>]+>', '', patern , 0, re.I)
    patern = re.sub(r'&#\d+;', ' ', patern , 0, re.I)
    reg_ex = re.compile(r"\w+",re.I)
# подсчёт полученных слов и запись из в словарь words_dict
for word in reg_ex.findall(patern):
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
# пересортировка словаря words_dict из new_dict
new_dict = sorted(words_dict.items(), key = operator.itemgetter(1), reverse = True)
words_dict = dict(new_dict)
# создание осей Х и Y графика из массивов
os_x, os_y = [], []
for k, v in words_dict.items():
    os_x.append(k)
    os_y.append(v)
del os_y[200:len(os_y)] # выборка 200 первых значений чисел
del os_x[200:len(os_x)] # выборка 200 первых повторяющихся слов
# построение самого графика
fig, ax = plt.subplots()
ax.bar(os_x, os_y)
plt.xticks(rotation=90, fontsize=5, horizontalalignment='center', alpha=.7)
plt.title("Столбчатая диаграмма повторений 200 слов", fontsize=22)
plt.xlabel("Слова")
plt.ylabel("Количество повторений")
fig.set_figwidth(15)
fig.set_figheight(6)
plt.grid()
plt.show()
