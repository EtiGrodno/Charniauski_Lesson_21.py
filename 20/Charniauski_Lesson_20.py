#ДЗ на понедельник (Ivanov_Lesson_20.py)
# Вы создаете БД для учета задач в команде разработки.
# Вам необходимо создать базу данных для хранения информации о задачах и их статусе.
# Каждая задача должна иметь уникальный идентификатор, название,
# описание и статус (выполнена или невыполнена).
#
# Напишите программу на языке Python,
# которая создает базу данных SQLite,
# добавляет в нее несколько задач и позволяет пользователю получать информацию о задачах.

import sqlite3
conn = sqlite3.connect('acc_tasks.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS task_table(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    status TEXT
    )'''
)
# name1 = 'Task_1'
# description1 = 'Это первая задача'
# status1 = 'Выполненна'
#
# name2 = 'Task_2'
# description2 = 'Это вторая задача'
# status2 = 'Не выполненна'
#
# name3 = 'Task_3'
# description3 = 'Это третья задача'
# status3 = 'Выполненна'
#
# cursor.execute(
#     '''INSERT INTO task_table(
#     name,
#     description,
#     status
#     ) VALUES(?,?,?)''',(name1,description1,status1))
# cursor.execute(
#     '''INSERT INTO task_table(
#     name,
#     description,
#     status
#     ) VALUES(?,?,?)''',(name2,description2,status2))
# cursor.execute(
#     '''INSERT INTO task_table(
#     name,
#     description,
#     status
#     ) VALUES(?,?,?)''',(name3,description3,status3))
# conn.commit()

cursor.execute('''SELECT * FROM task_table''')
k = cursor.fetchall()
for i in k:
    print(*i)

conn.close()



