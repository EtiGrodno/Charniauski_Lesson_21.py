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



def long(self, object):
    return len(str(object))
class my_hw:
    def recept(self, object):
        if isinstance(object, str):
            glasnyye = 'ауоыиэюяеёaeiouy'
            soglasnyye = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz'
            verification = sum(i.lower() in glasnyye for i in object)\
                * sum(i.lower() in soglasnyye for i in object)
            if verification <= long(self, object):
                return ''.join(char for char in object if char.lower() in glasnyye)
            else:
                return ''.join(char for char in object if char.lower() in soglasnyye)
        elif isinstance(object, int):
            digit_sum = sum(int(digit) for digit in str(object) if digit in '2468')
            return digit_sum * long(self, object)

test17 = my_hw()

test1 = test17.recept(123)
test2 = test17.recept('abcdef')
test3 = test17.recept('aфгщуиоаыdef')
print(test1)
print(test2)
print(test3)
