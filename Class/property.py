# 02/12/2021 work with property: record and reading property
# Свойство и на чтение и на запись
# В него можно записать через сеттер и прочитать через принт
# Для пользователя проперти будет виден, как атрибут, а не как метод

class MonthEasy:
    month = 0

def use_month_easy():
    Boris_birthday_month = MonthEasy()
    Denis_birthday_month = MonthEasy()
    Boris_birthday_month.month = 13
    Denis_birthday_month.month = 2
    print(Boris_birthday_month.month)
    print(Denis_birthday_month.month)

class Month:

    def __init__(self):
        pass

    @property
    def month(self):
        return self.number

    @month.setter
    def month(self,number):
        #if number >=1 and number<=12:
           self.number = number
           assert  number >=1 and number<=12, "неправильно введен месяц"

        #else:
           #print('Неправильно введен месяц')

def use_month_class():
    Boris_birthday_month = Month()
    Denis_birthday_month = Month()
    Boris_birthday_month.month = 1
    Denis_birthday_month.month = 4
    print(Boris_birthday_month.month)
    print(Denis_birthday_month.month)

class Date:

    def __init__(self):
        pass

    def set_date(self,date):
        number,month,year = date.split('.')
        self._number = int(number)
        self._month = int(month)
        self._year = int(year)


    def get_date(self):
        return '{}.{}.{}'.format(self._number,self._month,self._year)

def test_date():
    # number = '13.10.2021'
    # d = Date()
    # d. set_date(number)
    # print(d.get_date())
    # if number != d.get_date():
    #     return False

    # тестируем предстоящие нули
    number = '01.09.2021'
    d = Date()
    d. set_date(number)
    print(d.get_date())
    if number != d.get_date():
        return False

    return True


if test_date():
    print('sucsess')
else:
    print('fail')




#use_month_class()
#use_month_easy()