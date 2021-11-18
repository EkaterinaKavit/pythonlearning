#Классы/Наследование / Классовые переменные и переменные инстанса
# Классовые, регулярные, статик - методы

class Employee:

    num_of_emp = 0
    raise_amount = 1.04 # создаем отдельно классовую переменную, чтобы к ней был быстрый доступ)
#если данная величина используется во многих методах, то если ее надо исправить, это сложно сделать

# специальный метод-конструктор, используемый для инициализации.
#В качестве первого аргумента используется инстанс и по соглашению он называется self.
# После него остальные аргументы, какие нужны

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

        Employee.num_of_emp += 1
# вместо self.first могло использоваться self.fname = first

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # если написать просто raise_amount, то будет ошибка
# необходимо использовать либо ссылку на класс (Employee.raise_amount), либо на инстанс (self.raise_amount)
# when we try to access an attribute on an instance it will first check if the instance contains that attribute.
# if not , it will see if the class or any class that it inherits from contains that attribute.
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#(1.04,1.04,1.04)
#emp_1.raise_amount=1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# (1.04,1.05,1.04)

    def __repr__(self):
        return 'Employee({},{},{})'.format(self.first, self.last, self.pay)

    def __str__(self):
        return"Employee({}-{})".format(self.fullname(), self.pay)

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
# классовые методы используются как альтернативные конструкторы, чтобы создать множество способов создания объектов
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)
# Employee.set_raise_amt(1.2) это тоже самое, что Employee.raise_amount = 1.2
#классовые методы также можно запустить из инстанса,
# но это не имеет большого смысла и так не делают (emp_1.set_raise_amt(1.05))
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self,first,last,pay)(другой способ кроме функции super))
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        #self.first = first
        #self.last = last
        #self.pay = pay
        #super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Employee('Semen', 'Kozlov', 100000)
emp_2 = Employee('Maria', 'Slepakova', 80000)

print(len(emp_1))

#print(emp_1+emp_2)
#print(emp_1)
#print(repr(emp_1))
#print(str(emp_1))

#print(emp_1.__repr__())
#print(emp_1.__str__())
dev_1 = Developer('Ivan','Morozov',40000,'Python')
dev_2 = Developer('Olga','Avdeeva',100000, 'Java')

manager_1 = Manager('Jhon', 'Smith', 150000,[dev_1,dev_2])

print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)

print(manager_1.print_emp())
#manager_1.remove_emp(dev_2)
#print(manager_1.print_emp())

#print(dev_1.prog_lang)
#print(dev_2.email)
#print(help(Developer))


#print(dev_1.email)
#print(emp_1.Fullname())
#print(Employee.Fullname(emp_1))

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#emp_1.raise_amount=1.05
#Employee.raise_amount=1.1
#print(emp_1.__dict__)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#print(Employee.num_of_emp)

#emp_str_1 = 'Alena-Grigoryeva-10000'
#emp_str_2 = 'Gosha-Andreev-50000'

#new_emp_str = Employee.from_string(emp_str_1)
#print(new_emp_str.email)
#print(new_emp_str.pay)

