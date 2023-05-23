# ДЗ на четверг (Ivanov_Lesson_17.py) - на гитхаб
# Описать два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение количества гласных и согласных букв меньше или равно длине слова, то выводить все гласные,
# иначе согласные;
# если передаю число, то вывести произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.
# Итого - один класс, в нем только ДВА МЕТОДА
# Тест:
# object(123) --> 6
# object('abcdef') --> bcdf

class my_hw:
    def recept(self, object):
        def long(self, object):
            return len(str(object))
        if isinstance(object, str):
            if sum(i in 'ауоыиэюяеёaeiouy' for i in object.lower()) * sum(i
                    in 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz'
                    for i in object.lower()) <= long(self, object) :
                return ''.join([i for i in object if i.lower() in 'ауоыиэюяеёaeiouy'])
            else:
                return ''.join([i for i in object if i.lower() in 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz'])
        elif isinstance(object, int):
            return sum(int(i) for i in str(object) if i in '2468') * long(self, object)

test17 = my_hw()

test1 = test17.recept(123)
test2 = test17.recept('abcdef')
test3 = test17.recept('aфгщуиоаыdef')
print(test1)
print(test2)
print(test3)