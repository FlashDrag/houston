'''html таблица в Python
Обработка таблицы в целях автоматизации ручного ввода

Таблица (раздел: Экономика - Общее состояние):
`Крупнейшие компании, базирующиеся в Хьюстоне по версии Fortune 500 на 2016 год.`
1.Копируем текст таблицы с layout.pdf макета в table.csv
2.Парсим и сохраняем в table.html
3.C table.html вставляем готовый код html таблицы в основной html файл проекта
'''

# парсер
import csv

with open('table.csv') as csvfile:
    reader = csv.reader(csvfile)
    data = [row[0].split() for row in reader]

with open('table.html', 'w') as f:
    for lst in data:
        a = lst[0]
        c = lst[-1]
        b = ' '.join(lst[1:-1])

        f.write('<tr>\n')
        f.write(f'  <td>{a}</td>\n')
        f.write(f'  <td>{b}</td>\n')
        f.write(f'  <td>{c}</td>\n')
        f.write('</tr>\n')
