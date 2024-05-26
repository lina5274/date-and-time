#
# Создайте класс SuperDate, наследованный от класса datetime модуля datetime,
# объекты которого будут дополнительно обладать следующими методами:
#
# 1.  - должен возвращать сезон года (Summer, Autumn, Winter, Spring)
# 2. get_time_of_day - должен возвращать  время суток
# (Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6) (последнее число не включено в промежуток)
#
#
# Пример работы класса:
#
# a = SuperDate(2024, 2, 22, 12)
# print(a.get_season())
# print(a.get_time_of_day())
#
# Вывод на консоль:
# Winter
# Day
import datetime

class SuperDate(datetime.datetime):

    def get_season(self):
        m = self.month
        x = m%12 // 3+1
        if x == 1:
            return "Winter"
        if x == 2:
            return "Spring"
        if x == 3:
            return "Summer"
        if x == 4:
            return "Autumn"


    def get_time_of_day(self):
        time = self.hour
        if 6 < time < 12:
            return "Morning"
        elif 12 < time < 18:
            return "Day"
        elif 18 < time < 0:
            return "Evening"
        else:
            return "Night"

a = SuperDate(2024,5,26,15)
print(a.get_season())
print(a.get_time_of_day())









