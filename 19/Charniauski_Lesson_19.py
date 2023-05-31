#ДЗ на четверг (Ivanov_Lesson_19.py)
# Класс Company:
# Создайте класс Company
class Company:
    levels = {1:'junior',
              2:'middle',
              3:'senior',
              4:'lead'}

# Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации
# программиста: 1:junior, 2:middle, 3:senior, 4:lead.
# Создайте метод __init__(), внутри которого будут определены два protected свойства:
# 1) _index - передается параметром и
# 2) _level - принимает из словаря levels значение с ключом _index
# init(self, index)
# self._index = index
# self.level = levels[index]
    def __init__(self, index):
        self._index = index
        self._level = self.levels[index]
        print(index, self._level)

# Создайте метод _level_up(), который будет переводить программиста на следующий уровень
    def _level_up(self):
        if self._index in self.levels.keys():
            self._index += 1
            print(f' Уровень повышен: {self._index}')
        else:
            print (f' Максимальный уровень: {self._index}')
# Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
    def is_lead(self):
        if self._index == 4:
            print(f' Достигнут максимальный уровень: {self._level}')
# Класс Programmer:
# Создайте класс Programmer
# Создайте метод __init__(), внутри которого будут определены 3 динамических свойства:
# 1) name - передается параметром, является публичным,
# 2)age - возраст
# 3) level – уровень квалификации на основе словаря из Company
class Programmer(Company):
    def __init__(self, name, age, level):
        super().__init__(self.levels)
        self.name = name
        self.age = age
        level = self.levels
# Создайте метод work(), который заставляет программиста работать,
# что позволяет ему становиться более квалифицированным с помощью метода _level_up()
# родительского класса
    def work(self,level):
        level = self._level_up
# Создайте мeтод info(), который выведет информацию о вас: имя, возраст, квалификацию
    def info(self):
            print(
            f'Имя: {self.name}, '
            f'Возвраст: {self.age},'
            f'Уровень: {self._level},'
        )
# Создайте статический метод knowledge_base(), который выведет в консоль справку
# по программированию (просто любой текст).
    @staticmethod
    def knowledge_base():
            print('Усиленная работа повышает уровень!')
# Вызовите справку по программированию
# Создайте объекты классов Company и Programmer
# Используя объект класса Programmer, повысьте свой уровень квалификации
# Дойдите до уровня lead

#my_compani = Company(1)


my_programmer = Programmer('Виталий', 42)
