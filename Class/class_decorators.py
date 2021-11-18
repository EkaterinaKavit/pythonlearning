# Decorators/setters/deleters

class Employee:
    def __init__(self, first, last):
        self.f_name = first
        self.l_name = last

    @property # этот декоратор позволяет пользоваться методом как аттрибутом emp_1.email (без скобок)
    def email(self):
        return '{}.{}@company.com'.format(self.f_name, self.l_name)

    @property
    def fullname(self):
        return '{} {}'.format(self.f_name, self.l_name)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.f_name = first
        self.l_name = last

    @fullname.deleter
    def fullname(self):
        print("Deleted Name")
        self.f_name = None
        self.l_name = None

emp_1 = Employee('Jhon', 'Smith')
# emp_1.f_name = 'Jim'


# не позволяет пользоваться функцией как атрибутом несмотря на декоратор @property
emp_1.fullname = 'Corey Schafer'
# После использования @fullname.setter можно использовать метод, как аттрибут
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname  # использован deleter