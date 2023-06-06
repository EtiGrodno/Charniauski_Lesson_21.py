#_________________ДЗ на четверг (Ivanov_Lesson_21.py)
# _________________1. Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
# _________________Заполнить её с помощью INSERT данными (3 записи).
# _________________Удалить с помощью DELETE 2 запись. Обновить значения 3-ей записи на: hello world с помощью UPDATE
# _________________*Записать данные с таблицы в текстовый файл в три колонки. Первая – id, вторая и третья с данными

import sqlite3
conn = sqlite3.connect('table_3col.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS table_3col (id INTEGER PRIMARY KEY AUTOINCREMENT,
        test_text_1 TEXT,
        test_text_2 TEXT
                        )'''
)
i = 0
while i < 3:
    cursor.execute('''INSERT INTO table_3col (test_text_1,test_text_2) VALUES('первое поле','второе поле')''')
    i +=1
cursor.execute('''SELECT * FROM table_3col ''')
k = cursor.fetchall()
for j in k:
    if j[0] % 2 == 0:
        cursor.execute('''DELETE FROM table_3col WHERE id = ?''', (j[0],))
cursor.execute('''UPDATE table_3col SET test_text_2 = 'hello world' ''')
cursor.execute('''SELECT * FROM table_3col''')
conn.commit()
k = cursor.fetchall()
print(k)
for i in k:
    print(*i)
f = open('test_table_3col','w', encoding='utf-8')
for i in k:
    i = str(i)
    f.writelines(i + '\n')
f.close()
# conn.close()

# _________________# 2. В БД из первого задания удалить первую ПОЛОВИНУ записей, а вторую обновить на любые значения.
# ___________________ВРучную удалять нельзя!
# ___________________Если строк нечетное количество, то округляем в меньшую сторону!
from math import floor
cursor.execute('''SELECT * FROM table_3col ''')
summa = 0
for l in k:
     summa += l[0]
srednee = floor(summa/(len(k)*2))
print(srednee)
for n in k:
    if n[0] <= srednee:
        cursor.execute('''DELETE FROM table_3col WHERE id=?''',(n[0],))
        conn.commit()
    elif n[0] >= srednee:
        cursor.execute('''UPDATE table_3col SET test_text_1 = 'Всё что угодно 1 :)',
                        test_text_2 = 'Всё что угодно 2 :)' WHERE id=?''',(n[0],))
        conn.commit()
conn.close()

#3. Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
#  my_list = [‘Home’, ‘Work’, 29, 9, 2022]
# Если элемент списка слово, записать его в соответствующую таблицу,
# затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел,
# если нечётное, то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить первую запись в первой таблице.
# Если меньше, то обновить первую запись в первой таблице на «hello»

import sqlite3
conn1 = sqlite3.connect('table_3_1.db')
cursor1 = conn1.cursor()
cursor1.execute(
    '''CREATE TABLE IF NOT EXISTS table_3_1 (id INTEGER PRIMARY KEY AUTOINCREMENT,
        stroki TEXT
        )'''
)
conn2 = sqlite3.connect('table_3_2.db')
cursor2 = conn2.cursor()
cursor2.execute(
    '''CREATE TABLE IF NOT EXISTS table_3_2 (id INTEGER PRIMARY KEY AUTOINCREMENT,
        int INTEGER
       )'''
)
my_list = ['Home', 'Work', 29, 9, 2022]
for i in my_list:
    if type(i) == str:
        cursor1.execute('''INSERT INTO table_3_1(stroki) VALUES (?)''', (i,))
        a = len(i)
        cursor2.execute('''INSERT INTO table_3_2(int) VALUES (?)''', (a,))
        conn1.commit()
        conn2.commit()
    elif type(i) == int and i%2 == 0 :
        cursor2.execute('''INSERT INTO table_3_2(int) VALUES (?)''', (i,))
        conn2.commit()
    else:
        cursor1.execute('''INSERT INTO table_3_1(stroki) VALUES ('нечётное')''')
        conn1.commit()
cursor2.execute('''SELECT * FROM table_3_2 ''')
k = cursor2.fetchall()
if len(k) > 5:
    cursor1.execute('''DELETE FROM table_3_1 WHERE id=1''')
else:
    cursor1.execute('''UPDATE table_3_1 SET stroki = 'hello' WHERE id = 1''')
conn1.commit()
conn2.close()
conn1.close()