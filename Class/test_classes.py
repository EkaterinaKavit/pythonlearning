class CustomerProperty:

    def __init__(self):
        pass


    @property
    def name(self):
        return(self.__name)

    @name.setter
    def name(self, name):
        self.__name = name


class Customer:

    def __init__(self):
        pass

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class CustomerFish(Customer):

    def set_pay_way(self, pay):
        self.pay = pay
        if self.pay == 'cash':
            print('Client pays cash')
        if self.pay == 'e-card':
            print('Client pays e-card')

def main():

    cust= CustomerProperty()
    cust.name = 'nn'
    a = cust.name
    cust2 = CustomerFish()
    cust2.set_pay_way('cash')
    #cust1 = Customer()
    #cust1.set_name('Morozov')
    #print(cust1.get_name())

if __name__ == '__main__':
    main()