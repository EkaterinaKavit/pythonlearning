class Employee:
    amount_emp = 0

    def __init__(self, first, last, position, salary):
        self.first = first
        self.last = last
        self. position = position
        self.salary = salary
        #self.name_in_book = first+last+"-"+position+' of the Pizzeria'

        Employee.amount_emp += 1

    @property
    def fullname(self):
        return"{} {}".format(self.first, self.last)
    @property
    def name_in_book (self):
        return "{} {} - {} of the Pizzeria".format(self.first, self.last, self.position)
    @name_in_book.setter
    def name_in_book(self, name):
        a = len(name.split(' '))
        assert a == 3, "Аргумент функции должен содержать 3 слова: имя, фамилия, должность"
        #if a != 3:
            #print('Аргумент функции должен содержать 3 слова: имя, фамилия, должность')
        first, last, position = name.split(' ')
        self.first = first
        self.last = last
        self.position = position

    @name_in_book.deleter
    def name_in_book(self):
        print('Сотрудник удален')
        self.first = None
        self.last = None
        self.position = None


class Pizza:

    def __init__(self, name, composition = None):
        self.name = name

        if composition is None:
            self.composition = []
        else:
            self.composition = composition
    @property
    def ingredients(self):
        print('Состав пиццы', self.name, ':', self.composition)

    def add_ingredients(self, product):
        if product not in self.composition:
            self.composition.append(product)
            print(product, 'добавлен в состав пиццы', self.name)


emp_1 = Employee('Ivan', 'Morozov', 'chef', 200000)
emp_2 = Employee('Olga', 'Bobileva', 'waitress', 60000)
emp_3 = Employee('Igor', 'Korolev', 'waiter', 60000)
emp_1.name_in_book = 'Anna Bolshova waitress'


# it will "brake" program. Need make save setter for name_in_book
# cases:
#   1: if inapropriate argument "name" do nothing (не присваивать ничего если не корректно)
#   2: throw exception (проанализировать корректность аргумента name и выдать исклюючение если некорректно)
#      требуется изучение исключений. Пока не нужно делать. Но надо знать что такой вариант обработки\реакции существует
emp_1.name_in_book = 'Anna Bolshova chef'

print(emp_1.fullname)
print(emp_1.position)
print(emp_1.name_in_book)

#del emp_1.name_in_book

#print(Employee.amount_emp)

pizza_1 = Pizza("Margarita", ['chesse','tomatoes'])
pizza_2 = Pizza('Cezar', ['bekon','salat','cheese'])

#pizza_2.add_ingredients('onion')

