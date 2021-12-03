# how to create your own decorator
from datetime import datetime

def timeit(arg): # для ситуации, когда декоратор принимает значение name
#def timeit(func):
    print(arg) # для ситуации, когда декоратор принимает значение name
    def outer(func):# для ситуации, когда декоратор принимает значение name
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result #возвращает результат
        return wrapper # выдает обертку
    return outer # для ситуации, когда декоратор принимает значение name

@timeit('name')
def one(n):
    #start = datetime.now()
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    #print(datetime.now() - start)
    return (l)

@timeit('name') #например,'name' - гиперссылка
def two(n):
    #start = datetime.now()
    l = [x for x in range(n) if x % 2 == 0]
    #print(datetime.now() - start)
    return l

def main():
    #l1 = one(100)
    #l2 = two(100)

    #print(l1)
    #print(l2)

    #  функция как обьект
    #z = one
    #y = z(10)
    #print(y)

    # функция как аргумент, декораторы необходимо заключить в #
    #z1 = timeit(one)(10)
    #print(type(z1), z1.__name__)

    # декоратор принимает значения

    l= timeit('name')(one)(10)


if __name__ == '__main__':
    main()