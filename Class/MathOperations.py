class MathOperations:

    def __init__(self):
        pass

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b


def main():

    def test_use():
        a = 1
        b = 3
        result = 4
        num_test = MathOperations()
        sum1 = num_test.add(a,b)
        if sum1 != result:
            return False

        a = 4
        b = 2
        result = 2
        num_test = MathOperations()
        sub1 = num_test.sub(a, b)
        if sub1 != result:
            return False

        return True

    if test_use():
        print ('you made excellent programm')
    else:
        print('you made a mistake')

if __name__ == '__main__':
    main()

